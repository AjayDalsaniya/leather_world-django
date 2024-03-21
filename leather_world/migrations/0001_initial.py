# Generated by Django 5.0.3 on 2024-03-16 05:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('idcity', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('idnotification', models.AutoField(primary_key=True, serialize=False)),
                ('notification_description', models.TextField(blank=True, max_length=500)),
                ('notificationDate', models.DateField(null=True, verbose_name=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'notification',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('idoffer', models.AutoField(primary_key=True, serialize=False)),
                ('offer_value', models.DecimalField(decimal_places=0, max_digits=2)),
                ('offer_start_date', models.DateField()),
                ('offer_end_date', models.DateField()),
                ('offer_description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'offer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('idpurchase', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_total_amount', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('gst', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'purchase',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('idraw_material', models.AutoField(primary_key=True, serialize=False)),
                ('raw_material_name', models.CharField(max_length=60)),
                ('raw_materialtotal_quantity', models.IntegerField()),
                ('raw_material_price', models.IntegerField()),
            ],
            options={
                'db_table': 'raw_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('idtable', models.AutoField(primary_key=True, serialize=False)),
                ('table_capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'table',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TableReservation',
            fields=[
                ('idtable_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('tableResfname', models.CharField(max_length=150, null=True)),
                ('tableReslname', models.CharField(max_length=150, null=True)),
                ('tableResemail', models.CharField(max_length=150, null=True)),
                ('tableResmobile', models.CharField(max_length=150, null=True)),
                ('table_reservation_date_time', models.DateTimeField(null=True)),
                ('table_reservation_no_guest', models.IntegerField()),
                ('table_reservation_total_table_reserved', models.CharField(max_length=45)),
                ('total_amount', models.IntegerField(null=True)),
                ('is_table_reservation_cancel', models.IntegerField(default=0)),
                ('tableRes_payment_method', models.CharField(max_length=150)),
                ('tableRes_payment_id', models.CharField(max_length=250, null=True)),
                ('tableRes_status', models.CharField(default='Success', max_length=150)),
            ],
            options={
                'db_table': 'table_reservation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TotalGuest',
            fields=[
                ('idguest', models.AutoField(primary_key=True, serialize=False)),
                ('guestNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('pincode', models.DecimalField(decimal_places=0, max_digits=6, primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=100)),
                ('area_delivery_charges', models.IntegerField()),
                ('city_idcity', models.ForeignKey(db_column='city_idcity', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.city')),
            ],
            options={
                'db_table': 'area',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('iditem', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('item_price', models.IntegerField()),
                ('offer_price', models.FloatField(default=0)),
                ('item_description', models.CharField(max_length=200)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='media/item_images/')),
                ('offer_idoffer', models.ForeignKey(db_column='offer_idoffer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.offer')),
            ],
            options={
                'db_table': 'item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idorder', models.AutoField(primary_key=True, serialize=False)),
                ('orderfname', models.CharField(max_length=150, null=True)),
                ('orderlname', models.CharField(max_length=150, null=True)),
                ('orderemail', models.CharField(max_length=150, null=True)),
                ('ordermobile', models.CharField(max_length=150, null=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('cancel_order_date', models.DateTimeField(null=True)),
                ('order_delivery_date', models.DateTimeField(auto_now_add=True)),
                ('order_delivery_address', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('total_amount', models.FloatField()),
                ('order_payment_method', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=250, null=True)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Out for shipping', 'Out for shipping'), ('Completed', 'Completed')], default='Pending', max_length=150)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('is_cancel_order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('area_pincode', models.ForeignKey(db_column='area_pincode', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.area')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('item_iditem', models.ForeignKey(db_column='item_iditem', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.item')),
                ('order_idorder', models.ForeignKey(db_column='order_idorder', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.order')),
            ],
            options={
                'db_table': 'ordered_item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseReturn',
            fields=[
                ('idpurchase_return', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_return_total_amount', models.IntegerField()),
                ('purchase_return_date', models.DateField()),
                ('purchase_idpurchase', models.ForeignKey(db_column='purchase_idpurchase', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.purchase')),
            ],
            options={
                'db_table': 'purchase_return',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseReturnOfRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('purchase_return_idpurchase_return', models.ForeignKey(db_column='purchase_return_idpurchase_return', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.purchasereturn')),
                ('raw_material_idraw_material', models.ForeignKey(db_column='raw_material_idraw_material', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.rawmaterial')),
            ],
            options={
                'db_table': 'purchase_return_of_raw_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('purchase_idpurchase', models.ForeignKey(db_column='purchase_idpurchase', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.purchase')),
                ('raw_material_idraw_material', models.ForeignKey(db_column='raw_material_idraw_material', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.rawmaterial')),
            ],
            options={
                'db_table': 'purchase_raw_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('idrestaurant', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=45)),
                ('restaurant_email', models.CharField(max_length=45)),
                ('restaurant_phone', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('restaurant_description', models.CharField(max_length=200)),
                ('restaurant_image', models.ImageField(blank=True, null=True, upload_to='media/myImages/')),
                ('restaurant_address', models.CharField(max_length=500, null=True)),
                ('area_pincode', models.ForeignKey(db_column='area_pincode', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.area')),
            ],
            options={
                'db_table': 'restaurant',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='restaurant_idrestaurant',
            field=models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.restaurant'),
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('iditem_category', models.AutoField(primary_key=True, serialize=False)),
                ('item_category_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('item_category_description', models.CharField(max_length=1000)),
                ('item_category_image', models.ImageField(blank=True, null=True, upload_to='media/item_Category/')),
                ('restaurant_idrestaurant', models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.restaurant')),
            ],
            options={
                'db_table': 'item_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('idsubcategory', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('subcategory_description', models.CharField(max_length=1000)),
                ('subcategory_image', models.ImageField(blank=True, null=True, upload_to='media/subcategory/')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='leather_world.itemcategory')),
            ],
            options={
                'db_table': 'subcategory',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='item_category_iditem_category',
            field=models.ForeignKey(db_column='item_category_iditem_category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.subcategory'),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('idsupplier', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=60)),
                ('supplier_mobile_no', models.DecimalField(decimal_places=0, max_digits=10)),
                ('supplier_address', models.CharField(max_length=200)),
                ('area_name', models.CharField(max_length=200)),
                ('pincode', models.DecimalField(decimal_places=0, max_digits=6)),
                ('restaurant_idrestaurant', models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.restaurant')),
            ],
            options={
                'db_table': 'supplier',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier_idsupplier',
            field=models.ForeignKey(db_column='supplier_idsupplier', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.supplier'),
        ),
        migrations.CreateModel(
            name='TableReservationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_idtable', models.ForeignKey(db_column='table_idtable', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.table')),
                ('table_reservation_idtable_reservation', models.ForeignKey(db_column='table_reservation_idtable_reservation', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.tablereservation')),
            ],
            options={
                'db_table': 'table_reservation_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.AutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(max_length=25, null=True)),
                ('user_last_name', models.CharField(max_length=25, null=True)),
                ('user_name', models.CharField(max_length=15, unique=True)),
                ('user_password', models.CharField(max_length=300)),
                ('user_email', models.CharField(max_length=245, unique=True)),
                ('user_mobile', models.CharField(max_length=10, unique=True)),
                ('user_address', models.TextField(max_length=200, null=True)),
                ('user_sec_question', models.CharField(max_length=60, null=True)),
                ('user_sec_answer', models.CharField(max_length=60, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='media/myImages/')),
                ('is_admin', models.IntegerField()),
                ('forgot_password_token', models.CharField(default='', max_length=100)),
                ('idrestaurant', models.ForeignKey(db_column='restaurant_idrestaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.restaurant')),
                ('pincode', models.ForeignKey(db_column='area_pincode', default='362205', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.area')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tablereservation',
            name='user_iduser',
            field=models.ForeignKey(db_column='user_iduser', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.user'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('idreview', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('review_description', models.TextField(blank=True, max_length=500)),
                ('rating_value', models.FloatField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('reviewDate', models.DateField(null=True, verbose_name=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_iditem', models.ForeignKey(db_column='item_iditem', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.item')),
                ('user_iduser', models.ForeignKey(db_column='user_iduser', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.user')),
            ],
            options={
                'db_table': 'review',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user_iduser',
            field=models.ForeignKey(db_column='user_iduser', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.user'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_record', models.IntegerField(default=1)),
                ('item_qty', models.IntegerField()),
                ('item_iditem', models.ForeignKey(db_column='item_iditem', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.item')),
                ('user_iduser', models.ForeignKey(db_column='user_iduser', null=True, on_delete=django.db.models.deletion.SET_NULL, to='leather_world.user')),
            ],
            options={
                'db_table': 'cart',
                'managed': True,
            },
        ),
    ]
