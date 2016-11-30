from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import Textarea


class CardType(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='image/cardtype/%Y/%m/%d', blank=True)
    description = models.TextField( blank=True, null=True)
    orderview = models.PositiveIntegerField( blank=True, null=True)

    class Meta:
        ordering = ('id',)
        index_together = (('id', 'slug'),)
        #hien thi tren admin
        verbose_name = '01. Cart Type'
        verbose_name_plural = '01. Cart Types'

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('postage:cardtype_list', args=[self.id, self.slug])


class VehicleType(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='image/vehicletype/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, null=True)
    orderview = models.PositiveIntegerField( blank=True, null=True)

    class Meta:
        ordering = ('id',)
        index_together = (('id', 'slug'),)
        #hien thi tren admin
        verbose_name = '02. Vehicle Type'
        verbose_name_plural = '02. Vehicle Types'

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('postage:vehicletype_list', args=[self.id, self.slug])


#hãng xe
#[ID]
#  ,[TENHANG]
#  ,[NGAYDANGKY]
#  ,[NGAYBATDAU]
#  ,[NGAYKETTHUC]
#  ,[TRANGTHAI]
#  ,[SOCHODANGKY]
#  ,[THOIGIAN_CAPNHAT]
#  ,[TRANGTHAI_XULY]
#  ,[ID_LINK]
#  FROM [TCP_WEBAPP].[dbo].[DANHSACH_HANGXE_TAXI]
class VehicleSupplier(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(max_length=50, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    slotnumber = models.PositiveIntegerField(db_index=True)
    orderview = models.PositiveIntegerField(blank=True, null=True)
    #date
    registerdate = models.DateTimeField()
    enddate = models.DateTimeField()
    startdate = models.DateTimeField()
    infor = models.TextField(max_length=200, db_index=True, blank=True, null=True)
    status = models.CharField(max_length=5, db_index=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    idlink=models.PositiveIntegerField(db_index=True, blank=True, null=True)

    class Meta:
        ordering = ('id',)
        index_together = (('id', 'slug'),)
        #managed = True
        #db_table = 'vehiclesuppliers'
        #unique_together = [('taskid', 'update', 'sitename'),]
        #hien thi tren admin
        verbose_name = '03. Vehicle Supplier'
        verbose_name_plural = '03. Vehicle Suppliers'

    def __str__(self):
        #return self.name
        return '{}-{}'.format(self.id, self.name)


# Create your models here.
#[ID]
#  ,[LOAITHE]
#  ,[LOAIXE]
#  ,[BIENSOXE]
#  ,[THOIGIANVAO]
#  ,[THOIGIANRA]
#  ,[TRAMVAO]
#  ,[TRAMRA]
#  ,[TRANGTHAI]
#  ,[THOIGIAN_CAPNHAT]
#  ,[TRANGTHAI_XULY]
#  ,[ID_LINK]
class VehicleInOut(models.Model):
    id = models.AutoField(primary_key=True)
    cardtype = models.ForeignKey(CardType,  related_name='rel_vehio_cardtypes')
    vehicletype = models.ForeignKey(VehicleType, related_name='rel_vehio_vehicletypes')
    #neu chi giamsat vao ra doi voi phuongtien dangky tháng thì set FK,nguoc lai k cần khi đó tự nhap.
    vehiclenumber = models.CharField(max_length=10, db_index=True)

    checkin = models.DateTimeField()
    checkout=models.DateTimeField()
    stationnamein = models.CharField(max_length=50, db_index=True)
    stationnameout = models.CharField(max_length=50, db_index=True)
    status = models.CharField(max_length=5, db_index=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    idlink=models.PositiveIntegerField( db_index=True, blank=True, null=True)
    ##tcp chưa có 3column này, bo sung de demo
    payin = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)#tong so tien nạp vào
    charge = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)#tong so tien da sudung
    amount = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)#tong sotien co trong tk

    class Meta:
        #managed = True
        #db_table = 'vehicleinout'
        ordering = ('cardtype',)
        #index_together = (('id', 'vehiclenumber'),)
        #unique_together = [('taskid', 'update', 'sitename'),]
        #hien thi tren admin
        verbose_name = '--> Verhicle In/Out'
        verbose_name_plural = '--> Verhicle In/Out'


#xe tháng
#[ID]
#  ,[LOAITHE]
#  ,[LOAIXE]
#  ,[TENCHUXE]
#  ,[BIENSOXE]
#  ,[NGAYDANGKY]
#  ,[NGAYHETHAN]
#  ,[NGAYBATDAU]
#  ,[THONGTIN1]
#  ,[THONGTIN2]
#  ,[THONGTIN3]
#  ,[THOIGIAN_CAPNHAT]
#  ,[TRANGTHAI_XULY]
#  ,[ID_LINK]
class RegisteredVehicle(models.Model):
    id = models.AutoField( primary_key=True)
    #column nay tcp chua co, bosung mã thẻ: cardnumber
    cardnumber = models.CharField(max_length=50, db_index=True)

    cardtype = models.ForeignKey(CardType,  related_name='rel_vehc_cardtypes')
    vehicletype = models.ForeignKey(VehicleType,  related_name='rel_vehc_vehicletypes')
    vehicleowner = models.CharField(max_length=50, db_index=True)
    vehicleuser = models.ForeignKey(User, related_name='rel_vehu_users')
    vehiclesupplier= models.ForeignKey(VehicleSupplier,  related_name='rel_vehc_vehiclesuppliers')
    vehiclenumber = models.CharField(max_length=50, db_index=True)
    #date
    registerdate = models.DateTimeField()
    enddate=models.DateTimeField()
    startdate = models.DateTimeField()
    infor = models.TextField(max_length=200, db_index=True, blank=True, null=True)
    status = models.CharField(max_length=5, db_index=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    idlink=models.PositiveIntegerField( db_index=True, blank=True, null=True)

    class Meta:
        ordering = ('cardnumber',)
        index_together = (('cardnumber', 'vehiclenumber'),)
        #managed = True
        #db_table = 'vehiclecards'
        #unique_together = [('taskid', 'update', 'sitename'),]
        #hien thi tren admin
        verbose_name = '--> Registered Vehicle'
        verbose_name_plural = '--> Registered Vehicle'