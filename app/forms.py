from django.forms import ModelForm
from django import forms
from .models import basedata
from django.contrib.auth.models import User



class BaseForm(ModelForm):
    #updated_by = forms.CharField(initial=User.username) 
    updated_by = forms.ModelChoiceField(queryset=User.objects.distinct("username").all())

    class Meta:
       model = basedata
       fields = ['uniqueid','schoolid','district','upazilla','s_union','mouza','village','sheltername','constructionyear','northing','easting','fundingagencies','usesas','condition','noofvillage','acc_cap_per','acc_cap_livestock','plintharea','landarea','maletoilet','femaletoilet','watersupplystatus','watersupplysource','septictank','ramp','population','distance','expectedpopulation','warningsystem','warningsystemdetails','existing','underconstruction','ground','g_others','first','f_ohter','second','s_others','third','t_others','rs_ground','rs_first','rs_second','rs_roof','rs_beam','rs_column','rs_wall','rs_window','rs_door','rs_toilet','rs_stair','rs_ramp','rs_others','rs_ifothersfillup','communicationsource','cs_others','powerstation','ps_others','waterreservior','foodstoragesystem','additionaltoilet','septiktanksoakwell','others','polderwashedaway','polderrepaired','polderneedrepairs','road1from','road2from','road3from','road4from','road1to','road2to','road3to','road4to','road1name','road2name','road3name','road4name','road1type','road2type','road3type','road4type','road1id','road2id','road3id','road4id','road1length','road2length','road3length','road4length','road1pavement','road2pavement','road3pavement','road4pavement','road1embankment', 'road2embankment','road3embankment','road4embankment','road1kachcha','road2kachcha','road3kachcha','road4kachcha','road1bc','road2bc','road3bc','road4bc','road1other','road2other','road3other','road4other','road1surfacing','road2surfacing','road3surfacing','road4surfacing','road1basecourse','road2basecourse','road3basecourse','road4basecourse','road1sbase','road2sbase','road3sbase','road4sbase','road1roadcovered','road2roadcovered','road3roadcovered','road4roadcovered','road1avgdepth','road2avgdepth','road3avgdepth','road4avgdepth','e1_a','e1_b','e1_c','e2_a','e2_b','e2_c','e3_a','e3_b','e3_c','e4_a','e4_b','e4_c','e5_a','e5_b','e5_c','e6_a','e6_b','e6_c','e7_a','e7_b','e7_c','e8_a','e8_b','e8_c','e9_a','e9_b','e9_c','updated_by']




