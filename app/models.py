from django.db import models
from datetime import datetime  

# Create your models here.
class school_info(models.Model):
    unique_id = models.CharField(max_length=200)
    school_id = models.CharField(max_length=200)
    zilla = models.CharField(max_length=200)
    upazilla = models.CharField(max_length=200)
    mouza = models.CharField(max_length=200)
    union = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    no_of_village = models.IntegerField()
    construction_year = models.CharField(max_length=200)
    acc_cap_per = models.CharField(max_length=200)
    acc_cap_ls = models.CharField(max_length=200)
    plinth_area = models.FloatField()
    land_area = models.FloatField()
    northing = models.FloatField()
    easting = models.FloatField()
    population = models.IntegerField()
    distance = models.FloatField()
    expected_population = models.IntegerField()
    existing = models.IntegerField()
    under_construction =  models.IntegerField()
    ground_floor_uses = models.CharField(max_length=200)
    g_others_uses = models.CharField(max_length=200)
    first_floor_uses = models.CharField(max_length=200)
    f_others_uses = models.CharField(max_length=200)
    second_floor_uses = models.CharField(max_length=200)
    s_others_uses = models.CharField(max_length=200)
    third_floor_uses = models.CharField(max_length=200)
    t_others_uses = models.CharField(max_length=200)
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)

class school_repair_status(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    ground_floor = models.IntegerField()
    first_floor = models.IntegerField()
    second_floor = models.IntegerField()
    roof = models.IntegerField()
    beam = models.IntegerField()
    column = models.IntegerField()
    wall = models.IntegerField()
    windows = models.IntegerField()
    door = models.IntegerField()
    toilet = models.IntegerField()
    stair = models.IntegerField()
    ramp = models.IntegerField()
    others = models.IntegerField()
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)

class school_facilities(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    male_toilets = models.IntegerField()
    female_toilets = models.IntegerField()
    water_supply_status = models.IntegerField()
    water_source = models.IntegerField()
    septic_tank = models.IntegerField()
    ramp = models.IntegerField()
    warning_system = models.CharField(max_length=200)
    communication_system = models.CharField(max_length=200)
    comm_system_others = models.CharField(max_length=200)
    power_supply = models.CharField(max_length=200)
    ps_others = models.CharField(max_length=200)
    water_reservior = models.IntegerField()
    food_storage_system = models.IntegerField()
    additional_toilet = models.IntegerField()
    septik_tank_soak_well = models.IntegerField()
    others = models.CharField(max_length=200)
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)

class polder_inventory(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    polder_washed_away = models.CharField(max_length=200)
    polder_repaired = models.IntegerField()
    polder_need_repairs = models.IntegerField()
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)

class access_road(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    number = models.IntegerField()
    road_from = models.CharField(max_length=200)
    road_to = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    road_type = models.CharField(max_length=200)
    road_id = models.CharField(max_length=200)
    length = models.FloatField()
    pavement_width = models.FloatField()
    embankment_width = models.FloatField()
    kachcha = models.IntegerField()
    bc = models.IntegerField()
    others = models.CharField(max_length=200)
    surfacing = models.FloatField()
    base_course = models.FloatField()
    s_base = models.FloatField()
    road_covered = models.FloatField()
    avg_depth = models.FloatField()
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)

class environmental_screnning(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    e_1_answer = models.IntegerField()
    e_1_scale_of_impact = models.IntegerField()
    e_1_remarks = models.CharField(max_length=200)
    e_2_answer = models.IntegerField()
    e_2_scale_of_impact = models.IntegerField()
    e_2_remarks = models.CharField(max_length=200)
    e_3_answer = models.IntegerField()
    e_3_scale_of_impact = models.IntegerField()
    e_3_remarks = models.CharField(max_length=200)
    e_4_answer = models.IntegerField()
    e_4_scale_of_impact = models.IntegerField()
    e_4_remarks = models.CharField(max_length=200)
    e_5_answer = models.IntegerField()
    e_5_scale_of_impact = models.IntegerField()
    e_5_remarks = models.CharField(max_length=200)
    e_6_answer = models.IntegerField()
    e_6_scale_of_impact = models.IntegerField()
    e_6_remarks = models.CharField(max_length=200)
    e_7_answer = models.IntegerField()
    e_7_scale_of_impact = models.IntegerField()
    e_7_remarks = models.CharField(max_length=200)
    e_8_answer = models.IntegerField()
    e_8_scale_of_impact = models.IntegerField()
    e_8_remarks = models.CharField(max_length=200)
    e_9_answer = models.IntegerField()
    e_9_scale_of_impact = models.IntegerField()
    e_9_remarks = models.CharField(max_length=200)
    update_date  = models.DateTimeField(default=datetime.now, blank=True)
    updated_by = models.CharField(max_length=200)







class basedata(models.Model):
    uniqueid = models.CharField(max_length=200, blank=True)
    schoolid = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    upazilla = models.CharField(max_length=200, blank=True)
    s_union = models.CharField(max_length=200, blank=True)
    mouza = models.CharField(max_length=200, blank=True)
    village = models.CharField(max_length=200, blank=True)
    sheltername = models.CharField(max_length=200, blank=True)
    constructionyear = models.CharField(max_length=200, blank=True)
    northing = models.CharField(max_length=200, blank=True)
    easting = models.CharField(max_length=200, blank=True)
    fundingagencies = models.CharField(max_length=200, blank=True)
    usesas = models.CharField(max_length=200, blank=True)
    condition = models.CharField(max_length=200, blank=True)
    noofvillage = models.CharField(max_length=200, blank=True)
    acc_cap_per = models.CharField(max_length=200, blank=True)
    acc_cap_livestock = models.CharField(max_length=200, blank=True)
    plintharea = models.CharField(max_length=200, blank=True)
    landarea = models.CharField(max_length=200, blank=True)
    maletoilet = models.CharField(max_length=200, blank=True)
    femaletoilet = models.CharField(max_length=200, blank=True)
    watersupplystatus = models.CharField(max_length=200, blank=True)
    watersupplysource = models.CharField(max_length=200, blank=True)
    septictank = models.CharField(max_length=200, blank=True)
    ramp = models.CharField(max_length=200, blank=True)
    population = models.CharField(max_length=200, blank=True)
    distance = models.CharField(max_length=200, blank=True)
    expectedpopulation= models.CharField(max_length=200, blank=True)
    warningsystem = models.CharField(max_length=200, blank=True)
    warningsystemdetails = models.CharField(max_length=200, blank=True)
    existing = models.CharField(max_length=200, blank=True)
    underconstruction = models.CharField(max_length=200, blank=True)
    ground = models.CharField(max_length=200, blank=True)
    g_others = models.CharField(max_length=200, blank=True)   
    first = models.CharField(max_length=200, blank=True)
    f_ohter = models.CharField(max_length=200, blank=True)
    second = models.CharField(max_length=200, blank=True)
    s_others = models.CharField(max_length=200, blank=True)
    third = models.CharField(max_length=200, blank=True)   
    t_others = models.CharField(max_length=200, blank=True)
    rs_ground = models.CharField(max_length=200, blank=True)
    rs_first = models.CharField(max_length=200, blank=True)
    rs_second = models.CharField(max_length=200, blank=True)
    rs_roof = models.CharField(max_length=200, blank=True)   
    rs_beam = models.CharField(max_length=200, blank=True)
    rs_column = models.CharField(max_length=200, blank=True)
    rs_wall = models.CharField(max_length=200, blank=True)
    rs_window = models.CharField(max_length=200, blank=True)
    rs_door = models.CharField(max_length=200, blank=True)   
    rs_toilet= models.CharField(max_length=200, blank=True)
    rs_stair = models.CharField(max_length=200, blank=True)
    rs_ramp = models.CharField(max_length=200, blank=True)
    rs_others = models.CharField(max_length=200, blank=True)
    rs_ifothersfillup = models.CharField(max_length=200, blank=True)   
    communicationsource = models.CharField(max_length=200, blank=True)
    cs_others = models.CharField(max_length=200, blank=True)
    powerstation = models.CharField(max_length=200, blank=True)
    ps_others = models.CharField(max_length=200, blank=True)
    waterreservior = models.CharField(max_length=200, blank=True)   
    foodstoragesystem = models.CharField(max_length=200, blank=True)
    additionaltoilet = models.CharField(max_length=200, blank=True)
    septiktanksoakwell = models.CharField(max_length=200, blank=True)
    others = models.CharField(max_length=200, blank=True)
    polderwashedaway = models.CharField(max_length=200, blank=True)   
    polderrepaired = models.CharField(max_length=200, blank=True)
    polderneedrepairs = models.CharField(max_length=200, blank=True)
    road1from = models.CharField(max_length=200, blank=True)
    road2from = models.CharField(max_length=200, blank=True)
    road3from = models.CharField(max_length=200, blank=True)
    road4from = models.CharField(max_length=200, blank=True)
    road1to = models.CharField(max_length=200, blank=True)
    road2to = models.CharField(max_length=200, blank=True)
    road3to = models.CharField(max_length=200, blank=True)
    road4to = models.CharField(max_length=200, blank=True)
    road1name = models.CharField(max_length=200, blank=True)
    road2name = models.CharField(max_length=200, blank=True)
    road3name = models.CharField(max_length=200, blank=True)
    road4name = models.CharField(max_length=200, blank=True)
    road1type = models.CharField(max_length=200, blank=True)
    road2type = models.CharField(max_length=200, blank=True)
    road3type = models.CharField(max_length=200, blank=True)
    road4type = models.CharField(max_length=200, blank=True)
    road1id = models.CharField(max_length=200, blank=True)
    road2id = models.CharField(max_length=200, blank=True)
    road3id = models.CharField(max_length=200, blank=True)
    road4id = models.CharField(max_length=200, blank=True)
    road1length = models.CharField(max_length=200, blank=True)
    road2length = models.CharField(max_length=200, blank=True)
    road3length = models.CharField(max_length=200, blank=True)
    road4length = models.CharField(max_length=200, blank=True)
    road1pavement = models.CharField(max_length=200, blank=True)
    road2pavement = models.CharField(max_length=200, blank=True)
    road3pavement = models.CharField(max_length=200, blank=True)
    road4pavement = models.CharField(max_length=200, blank=True)
    road1embankment = models.CharField(max_length=200, blank=True)
    road2embankment = models.CharField(max_length=200, blank=True)
    road3embankment = models.CharField(max_length=200, blank=True)
    road4embankment = models.CharField(max_length=200, blank=True)
    road1kachcha = models.CharField(max_length=200, blank=True)
    road2kachcha = models.CharField(max_length=200, blank=True)
    road3kachcha = models.CharField(max_length=200, blank=True)
    road4kachcha = models.CharField(max_length=200, blank=True)
    road1bc=  models.CharField(max_length=200, blank=True)
    road2bc=  models.CharField(max_length=200, blank=True)
    road3bc=  models.CharField(max_length=200, blank=True)
    road4bc=  models.CharField(max_length=200, blank=True)
    road1other=  models.CharField(max_length=200, blank=True)
    road2other=  models.CharField(max_length=200, blank=True)
    road3other=  models.CharField(max_length=200, blank=True)
    road4other=  models.CharField(max_length=200, blank=True)
    road1surfacing=  models.CharField(max_length=200, blank=True)
    road2surfacing=  models.CharField(max_length=200, blank=True)
    road3surfacing=  models.CharField(max_length=200, blank=True)
    road4surfacing=  models.CharField(max_length=200, blank=True)
    road1basecourse=  models.CharField(max_length=200, blank=True)
    road2basecourse=  models.CharField(max_length=200, blank=True)
    road3basecourse=  models.CharField(max_length=200, blank=True)
    road4basecourse=  models.CharField(max_length=200, blank=True)
    road1sbase=  models.CharField(max_length=200, blank=True)
    road2sbase=  models.CharField(max_length=200, blank=True)
    road3sbase=  models.CharField(max_length=200, blank=True)
    road4sbase=  models.CharField(max_length=200, blank=True)
    road1roadcovered=  models.CharField(max_length=200, blank=True)
    road2roadcovered=  models.CharField(max_length=200, blank=True)
    road3roadcovered=  models.CharField(max_length=200, blank=True)
    road4roadcovered=  models.CharField(max_length=200, blank=True)
    road1avgdepth=  models.CharField(max_length=200, blank=True)
    road2avgdepth=  models.CharField(max_length=200, blank=True)
    road3avgdepth=  models.CharField(max_length=200, blank=True)
    road4avgdepth=  models.CharField(max_length=200, blank=True)    
    e1_a=  models.CharField(max_length=200, blank=True)
    e1_b=  models.CharField(max_length=200, blank=True)
    e1_c=  models.CharField(max_length=200, blank=True)
    e2_a=  models.CharField(max_length=200, blank=True)
    e2_b=  models.CharField(max_length=200, blank=True)
    e2_c=  models.CharField(max_length=200, blank=True)
    e3_a=  models.CharField(max_length=200, blank=True)
    e3_b=  models.CharField(max_length=200, blank=True)
    e3_c=  models.CharField(max_length=200, blank=True)
    e4_a=  models.CharField(max_length=200, blank=True)
    e4_b=  models.CharField(max_length=200, blank=True)
    e4_c=  models.CharField(max_length=200, blank=True)
    e5_a=  models.CharField(max_length=200, blank=True)
    e5_b=  models.CharField(max_length=200, blank=True)
    e5_c=  models.CharField(max_length=200, blank=True)
    e6_a=  models.CharField(max_length=200, blank=True)
    e6_b=  models.CharField(max_length=200, blank=True)
    e6_c=  models.CharField(max_length=200, blank=True)
    e7_a=  models.CharField(max_length=200, blank=True)
    e7_b=  models.CharField(max_length=200, blank=True)
    e7_c=  models.CharField(max_length=200, blank=True)
    e8_a=  models.CharField(max_length=200, blank=True)
    e8_b=  models.CharField(max_length=200, blank=True)
    e8_c=  models.CharField(max_length=200, blank=True)
    e9_a=  models.CharField(max_length=200, blank=True)
    e9_b=  models.CharField(max_length=200, blank=True)
    e9_c=  models.CharField(max_length=200, blank=True)
    updated_by = models.CharField(max_length=200, blank=True)
    