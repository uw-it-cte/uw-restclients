from restclients.models.r25 import Event, BindingReservation
from restclients.r25 import nsmap, get_resource
from restclients.r25.reservations import reservations_from_xml
from urllib import urlencode


def get_event_by_id(event_id):
    url = "/r25ws/servlet/wrd/run/event.xml?event_id=%s" % event_id
    return events_from_xml(get_resource(url))[0]

def get_event_by_alien_uid(alien_uid):
    url = "/r25ws/servlet/wrd/run/event.xml?alien_uid=%s" % quote(alien_uid)
    return events_from_xml(get_resource(url))[0]

def get_events(**kwargs):
    """
    Return a list of events matching the passed filter. Supported kwargs are:

        parent_id (integer)
    """
    url = "/r25ws/servlet/wrd/run/events.xml"
    if len(kwargs):
        url += "?%s" % urlencode(kwargs)

    return events_from_xml(get_resource(url))

def events_from_xml(tree):
    events = []
    for node in tree.xpath("//r25:event", namespaces=nsmap):
        event = Event()
        event.event_id = node.xpath("r25:event_id", namespaces=nsmap)[0].text
        event.alien_uid = node.xpath("r25:alien_uid", namespaces=nsmap)[0].text
        event.name = node.xpath("r25:event_name", namespaces=nsmap)[0].text
        event.title = node.xpath("r25:event_title", namespaces=nsmap)[0].text
        event.start_date = node.xpath("r25:start_date",
                                      namespaces=nsmap)[0].text
        event.end_date = node.xpath("r25:end_date", namespaces=nsmap)[0].text
        event.state = node.xpath("r25:state", namespaces=nsmap)[0].text
        event.parent_id = node.xpath("r25:parent_id", namespaces=nsmap)[0].text
        event.cabinet_id = node.xpath("r25:cabinet_id",
                                      namespaces=nsmap)[0].text
        event.cabinet_name = node.xpath("r25:cabinet_name",
                                        namespaces=nsmap)[0].text

        try:
            pnode = node.xpath("r25:profile", namespaces=nsmap)[0]
            event.binding_reservations = binding_reservations_from_xml(pnode)
            event.reservations = reservations_from_xml(pnode)
        except IndexError:
            event.binding_reservations = []
            event.reservations = []

        events.append(event)

    return events

def binding_reservations_from_xml(tree):
    binding_reservations = []
    for node in tree.xpath("//r25:binding_reservation", namespaces=nsmap):
        br = BindingReservation()
        br.bound_reservation_id = node.xpath("r25:bound_reservation_id",
                                             namespaces=nsmap)[0].text
        br.primary_reservation = node.xpath("r25:primary_reservation",
                                            namespaces=nsmap)[0].text
        br.name = node.xpath("r25:bound_name", namespaces=nsmap)[0].text
        br.bound_event_id = node.xpath("r25:bound_event_id",
                                       namespaces=nsmap)[0].text
        binding_reservations.append(br)

    return binding_reservations
