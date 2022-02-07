from django.views.generic import CreateView

from clients.models import Client


class AddClientView(CreateView):
    model = Client
    fields = ['account_id']
    template_name = 'code_challenge/add_client.html'
    success_url = 'add_client'

    def form_valid(self, form, **kwargs):
        data = form.cleaned_data
        account_id = data['account_id']
        last_created_client = Client.objects.latest('id')
        print(last_created_client)
        last_created_client_one_to_fifteen = last_created_client.one_to_fifteen_slot
        if last_created_client_one_to_fifteen >= 15:
            form.instance.one_to_fifteen_slot = 1
        else:
            form.instance.one_to_fifteen_slot = last_created_client_one_to_fifteen + 1
        print('Creating new client with account_id: {0}, one_to_fifteen_slot: {1}'.format(account_id, form.instance.one_to_fifteen_slot))
        form.save()
        context = self.get_context_data(**kwargs)
        context['status'] = 'Created new client with account_id: {0}, one_to_fifteen_slot: {1}'.format(account_id, form.instance.one_to_fifteen_slot)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddClientView, self).get_context_data(**kwargs)
        return context
