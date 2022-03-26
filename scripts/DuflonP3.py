from accounts import models as accounts_models
from meter_readings import models as meter_models

org_name = "DUFLON"
plant_name = "Duflon Industries Pvt Ltd , Mahad Unit -2"
org_initial = "DUFLON"
domain_name = "duflon.com"
device_domain_name = "duflon.com"  # ideally it should same as domain name

org_obj = accounts_models.Organisation.objects.get(name=org_name)

# device constant
device_email_domain_name = "@" + device_domain_name
device_initials = "Duflon"  # Use camel case for names
device_1_name = device_initials + "P3Controller1"

# create HT meter
ht_meter_connected = [
    # device 1
    {
        "organisation": org_obj,
        "device": accounts_models.Device.objects.get(user__username=device_1_name),
        "application_type": 1,  # transformer
        "details": "details not recorded",
        "modbus_slave_id": 11,
        "rated_kva": 315,
        "efficiency": 0.99,
        "no_load_loss": 0.7,
        "full_load_loss": 4.2,
        "application_details": {"testing": "testing"},
        "name": "Transformer 1 315 kVA",
    }

]

for ht_meter in ht_meter_connected:
    meter_models.HighTensionMeter.objects.create(**ht_meter)

# create Sub meter
ht_meter_1 = meter_models.HighTensionMeter.objects.get(name="Transformer 1 315 kVA")


sub_meter_connected = [
    {
        "organisation": org_obj,
        "application_type": 1,
        "device": accounts_models.Device.objects.get(user__username=device_1_name),
        "details": "details not recorded",
        "modbus_slave_id": 21,
        "rated_kva": 41.15,
        "efficiency": 0.99,
        "application_details": {"testing": "testing"},
        "ht_meter": ht_meter_1,
        "name": "ISO Machine",
    },
    {
        "organisation": org_obj,
        "application_type": 1,
        "device": accounts_models.Device.objects.get(user__username=device_1_name),
        "details": "details not recorded",
        "modbus_slave_id": 22,
        "rated_kva": 65.32,
        "efficiency": 0.99,
        "application_details": {"testing": "testing"},
        "ht_meter": ht_meter_1,
        "name": "PFA Panel Total",
    },
    {
        "organisation": org_obj,
        "application_type": 1,
        "device": accounts_models.Device.objects.get(user__username=device_1_name),
        "details": "details not recorded",
        "modbus_slave_id": 23,
        "rated_kva": 137.5,
        "efficiency": 0.99,
        "application_details": {"testing": "testing"},
        "ht_meter": ht_meter_1,
        "name": "PU Casting Total",
    }
    

]

for sub_meter in sub_meter_connected:
    meter_models.SubMeter.objects.create(**sub_meter)