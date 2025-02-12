from django import forms
from .models import cs_dep
from.models import csdep_sem2
from.models import csdep_sem3
from.models import csdep_sem4
from.models import csdep_sem5
from .models import csdep_sem6
class cs_sem1(forms.ModelForm):
    class Meta:
        model=cs_dep
        fields=[
            "stuname",
            "regno",
            "stuclass",
            "sub1",
            "sub2",
            "sub3",
            "sub4",
            "sub5",
        ]

class cs_sem2(forms.ModelForm):
    class Meta:
        model = csdep_sem2
        fields = [
            "stuname",
            "regno",
            "stuclass",
            "sub6",
            "sub7",
            "sub8",
            "sub9",
            "sub10",
        ]

class cs_sem3(forms.ModelForm):
    class Meta:
        model = csdep_sem3
        fields = [
            "stuname",
            "regno",
            "stuclass",
            "sub11",
            "sub12",
            "sub13",
            "sub14",
            "sub15",
        ]

class cs_sem4(forms.ModelForm):
    class Meta:
        model = csdep_sem4
        fields = [
            "stuname",
            "regno",
            "stuclass",
            "sub16",
            "sub17",
            "sub18",
            "sub19",
            "sub20",
            ]
class cs_sem5(forms.ModelForm):
    class Meta:
        model = csdep_sem5
        fields = [
            "stuname",
            "regno",
            "stuclass",
            "sub21",
            "sub22",
            "sub23",
            "sub24",
            "sub25",
            ]
class cs_sem6(forms.ModelForm):
    class Meta:
        model = csdep_sem6
        fields = [
            "stuname",
            "regno",
            "stuclass",
            "sub26",
            "sub27",
            "sub28",
            "sub29",
            "sub30",
            ]

