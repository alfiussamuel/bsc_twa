# See LICENSE file for full copyright and licensing details.
"""Res Users Models."""

from odoo import _, fields, api, models
from odoo.exceptions import UserError

class SalePartnerCategory(models.Model):
    _name = 'sale.partner.category'

    name = fields.Char('Customer Category')
    description = fields.Char('Description')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    year = fields.Integer('Year')
    color = fields.Many2one('color.color', string='Color')
    brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')
    model_id = fields.Many2one('fleet.vehicle.model', string='Model')
    periode_sewa = fields.Selection([
        ('Mingguan','Mingguan'),
        ('Bulanan','Bulanan'),
        ('Tahunan','Tahunan'),
    ], string="Periode Sewa")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    year = fields.Integer('Year')
    color = fields.Many2one('color.color', string='Color')
    brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')
    model_id = fields.Many2one('fleet.vehicle.model', string='Model')
    siup = fields.Char('Nomor SIUP')
    tdp = fields.Char('Nomor TDP')
    npwp = fields.Char('Nomor NPWP')
    nib = fields.Char('Nomor NIB')
    nama_direktur = fields.Char('Nama Direktur')
    ktp_direktur = fields.Char('KTP Direktur')
    tanggal_penagihan = fields.Char('Tanggal Penagihan')
    nomor_jaminan = fields.Char('Jaminan Penawaran')
    partner_category_id = fields.Many2one("sale.partner.category", string="Kategori Customer")

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def read_group(self):
        """Read group method."""
        data_obj = self.env['ir.model.data']
        result = super(ResUsers, self).read_group()
        try:
            dummy, group_id = data_obj.sudo().get_object_reference('product', 'group_uom')
            result.append(group_id)
        except ValueError:
            pass
        return result

    _defaults = {
        'groups_id': read_group,
    }


class ResPartner(models.Model):
    _inherit = 'res.partner'

    d_id = fields.Char(string='ID-Card')
    is_driver = fields.Boolean(string='Is Driver')
    insurance = fields.Boolean(string='Insurance')
    benefit = fields.Float('Benefit')
    salary = fields.Float('Salary')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    partner_id = fields.Many2one('res.partner', 'Current Customer')
    alamat_domisili = fields.Text('Alamat Domisili')
    cutoff_date = fields.Date('Cutoff Date')

class DriverAttendance(models.Model):
    _name = 'driver.attendance'

    date = fields.Date('Date', default=fields.Date.today())
    partner_id = fields.Many2one('res.partner', 'Driver', domain=[('is_driver', '=', True)])
    start_date = fields.Datetime('Start')
    end_date = fields.Datetime('Finish')

class DriverJob(models.Model):
    _name = 'driver.job'

    name = fields.Char('Job Description')

class DriverRequest(models.Model):
    _name = 'driver.request'

    name = fields.Char('Document No.')
    user_id = fields.Many2one('res.users', 'Request by', default=lambda self: self.env.user)
    date = fields.Date('Request Date', default=fields.Date.today())
    start_date = fields.Datetime('Start', default=fields.Date.today())
    end_date = fields.Datetime('Finish', default=fields.Date.today())
    arrival_time = fields.Datetime('Arrival Time', default=fields.Date.today())
    date = fields.Datetime('Finish', default=fields.Date.today())
    partner_id = fields.Many2one('res.partner', 'Driver', domain=[('is_driver', '=', True)])
    notes = fields.Text('Notes')
    customer_id = fields.Many2one('res.partner', 'Customer')
    contact_name = fields.Char('Contact Name')
    contact_phone = fields.Char('Phone Number')
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle')
    vehicle2_id = fields.Many2one('fleet.vehicle', 'Vehicle 2')
    address = fields.Char('Alamat Customer')
    job_id = fields.Many2one('driver.job', string='Job Desc')
    job2_id = fields.Many2one('driver.job', string='Job Desc 2')
    google_url = fields.Char('Google Maps URL')
    state = fields.Selection([
        ('Draft','Draft'),
        ('In Progress','In Progress'),
        ('Done','Done'),
        ('Cancelled','Cancelled')
    ], default='Draft', string="Status")

    def get_sequence(self, name=False, obj=False, context=None):
        sequence_id = self.env['ir.sequence'].search([
            ('name', '=', name),
            ('code', '=', obj),
            ('suffix', '=', '.DR/%(month)s/%(year)s')
        ])
        if not sequence_id :
            sequence_id = self.env['ir.sequence'].sudo().create({
                'name': name,
                'code': obj,
                'implementation': 'no_gap',
                'suffix': '.DR/%(month)s/%(year)s',
                'padding': 3
            })
        return sequence_id.next_by_id()

    @api.model
    def create(self, vals):
        vals['name'] = self.get_sequence('Driver Request Form', 'driver.request')
        return super(DriverRequest, self).create(vals)

    def action_progress(self):
        self.write({'state': 'In Progress'})

    def action_done(self):
        self.write({'state': 'Done'})

    def action_cancel(self):
        self.write({'state': 'Cancelled'})

class VehicleComponent(models.Model):
    _name = 'vehicle.component'

    name = fields.Char('Component Name')

class VehicleOperationType(models.Model):
    _name = 'vehicle.operation.type'

    name = fields.Char('Operation Type')

class VehicleCheckLine(models.Model):
    _name = 'vehicle.check.line'

    reference = fields.Many2one('vehicle.check', string='Reference')
    component_id = fields.Many2one('vehicle.component', string='Nama Komponen')
    is_checked_b = fields.Boolean('B', default=True)
    is_checked_r = fields.Boolean('R', default=False)
    is_checked_h = fields.Boolean('H', default=False)
    is_checked_t = fields.Boolean('T', default=False)

class VehicleCheck(models.Model):
    _name = 'vehicle.check'

    reference = fields.Many2one('fleet.vehicle', string='Reference')
    user_id = fields.Many2one('res.users', 'Created by', default=lambda self: self.env.user)
    tanggal_serah_terima = fields.Date('Date', default=fields.Date.today())
    operation_type_id = fields.Many2one('vehicle.operation.type', string='Operation Type')
    line_ids = fields.One2many('vehicle.check.line', 'reference', string='Lines')
    kode_ban_kanan_depan = fields.Char('Kanan Depan')
    kode_ban_kanan_belakang = fields.Char('Kanan Belakang')
    kode_ban_kiri_depan = fields.Char('Kiri Depan')
    kode_ban_kiri_belakang = fields.Char('Kiri Belakang')
    kode_ban_serep = fields.Char('Ban Serep')
    kode_accu = fields.Char('Kode Accu')
    
class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    check_ids = fields.One2many('vehicle.check', 'reference', string='Checks')

class VehicleGatePass(models.Model):
    _name = 'vehicle.gate.pass'

    name = fields.Char('Document No.')
    user_id = fields.Many2one('res.users', 'Request by', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.users', 'Pengguna Kendaraan')
    date = fields.Date('Request Date', default=fields.Date.today())
    tanggal_keluar = fields.Datetime('Tanggal Keluar', default=fields.Date.today())
    notes = fields.Char('Keperluan')
    kilometer = fields.Float('Km')
    bensin = fields.Selection([
        ('E','E'),
        ('1/8','1/8'),
        ('1/4','1/4'),
        ('1/2','1/2'),
        ('3/4','3/4'),
        ('F','F'),
    ], defaul='E', string='Bensin')
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle')
    
    def get_sequence(self, name=False, obj=False, context=None):
        sequence_id = self.env['ir.sequence'].search([
            ('name', '=', name),
            ('code', '=', obj),
            ('suffix', '=', '.GP/%(month)s/%(year)s')
        ])
        if not sequence_id :
            sequence_id = self.env['ir.sequence'].sudo().create({
                'name': name,
                'code': obj,
                'implementation': 'no_gap',
                'suffix': '.GP/%(month)s/%(year)s',
                'padding': 3
            })
        return sequence_id.next_by_id()

    @api.model
    def create(self, vals):
        vals['name'] = self.get_sequence('Gate Pass Form', 'vehicle.gate.pass')
        return super(VehicleGatePass, self).create(vals)

class VehicleStnkType(models.Model):
    _name = 'vehicle.stnk.type'

    name = fields.Char('Document Type')

class VehicleStnk(models.Model):
    _name = 'vehicle.stnk'
    _order = 'next_year_date asc'

    name = fields.Char('Document No.')    
    document_type = fields.Char(string="Document Type")
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle')
    next_year_date = fields.Date('Jatuh Tempo')
    next_5year_date = fields.Date('Tempo 5 Thn')
    
    biaya_b2nkb = fields.Float('B2N.KB')
    biaya_pkb = fields.Float('PKB')
    biaya_swdkllj = fields.Float('SWDLLJ')
    biaya_adm_stnk = fields.Float('Adm STNK')
    biaya_adm_tnkb = fields.Float('Adm TNKB')
    biaya_lain = fields.Float('Biaya Lain')
    biaya_lain_notes = fields.Char('Notes Biaya Lain')
    biaya_stnk = fields.Float(compute="_get_biaya_stnk", string='Total Biaya')

    biaya_jasa_raharja = fields.Float('Jasa Raharja')
    biaya_notice = fields.Float('Notice')
    biaya_acc_bdn = fields.Float('ACC BDN')
    total_biaya_notice = fields.Float(compute="_get_biaya_stnk", string='Total Biaya Notice')

    interval = fields.Selection([
        ('1 Bulan', '1 Bulan'),
        ('3 Bulan', '3 Bulan'),
        ('6 Bulan', '6 Bulan'),
        ('1 Tahun', '1 Tahun'),
    ], default='1 Tahun', string="Interval Jatuh Tempo")

    @api.depends('biaya_b2nkb','biaya_pkb','biaya_swdkllj',
        'biaya_adm_stnk','biaya_adm_tnkb','biaya_lain',
        'biaya_jasa_raharja','biaya_notice','biaya_acc_bdn')
    def _get_biaya_stnk(self):
        for res in self:
            res.biaya_stnk = res.biaya_notice + res.biaya_b2nkb + res.biaya_pkb + res.biaya_swdkllj + res.biaya_adm_stnk + res.biaya_adm_tnkb + res.biaya_lain
            res.total_biaya_notice = res.biaya_jasa_raharja + res.biaya_notice + res.biaya_acc_bdn

    def post_expense(self):
        return True

class VehicleKir(models.Model):
    _name = 'vehicle.kir'
    _order = 'next_year_date asc'

    name = fields.Char('Document No.')    
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle')
    next_year_date = fields.Date('Jatuh Tempo')
    biaya_stnk = fields.Float('Biaya KIR')
    biaya_pungli = fields.Float('Biaya Pungli')
    biaya_luar_kota = fields.Float('Biaya Luar Kota')
    interval = fields.Selection([
        ('1 Bulan', '1 Bulan'),
        ('3 Bulan', '3 Bulan'),
        ('6 Bulan', '6 Bulan'),
        ('1 Tahun', '1 Tahun'),
    ], default='1 Tahun', string="Interval Jatuh Tempo")

    def post_expense(self):
        return True

class VehicleIbm(models.Model):
    _name = 'vehicle.ibm'
    _order = 'next_year_date asc'

    name = fields.Char('Document No.')    
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle')
    next_year_date = fields.Date('Jatuh Tempo')
    biaya_stnk = fields.Float('Biaya Dokumen')
    interval = fields.Selection([
        ('1 Bulan', '1 Bulan'),
        ('3 Bulan', '3 Bulan'),
        ('6 Bulan', '6 Bulan'),
        ('1 Tahun', '1 Tahun'),
    ], default='6 Bulan', string="Interval Jatuh Tempo")

    def post_expense(self):
        return True