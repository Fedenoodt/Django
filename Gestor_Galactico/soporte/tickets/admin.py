from django.contrib import admin

from .models import Cliente, Ticket

class ClienteAdm(admin.ModelAdmin):
	list_display = ('nombre', 'dni', 'telefono', 'mail')
	search_fields = ('nombre', 'dni', 'telefono', 'mail')
	
class TicketAdm(admin.ModelAdmin):
	list_display = ('cliente_fk', 'fechahora', 'estado', 'descripcion')
	list_filter = ('estado',)
	
admin.site.register(Cliente, ClienteAdm)
admin.site.register(Ticket, TicketAdm)
