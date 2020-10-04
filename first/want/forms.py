from django import forms


class add_items(forms.Form):

    item_name = forms.CharField()

    def clean_item_name(self):
        data = self.cleaned_data['item_name'].lower()

        if data.isnumeric():
            raise ValidationError(_('Name of item can not be just numbers'))

        return data


class del_items(forms.Form):

    item_no = forms.IntegerField()


class update_items(forms.Form):

    item_no = forms.IntegerField()
    item_name = forms.CharField()

    def clean_item_name(self):
        data = self.cleaned_data['item_name'].lower()

        if data.isnumeric():
            raise ValidationError(_('Name of item can not be just numbers'))

        return data
    
    def clean_item_no(self):

        data = self.cleaned_data['item_no']
        
        return data


        
        