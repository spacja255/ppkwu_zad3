# PPKWU - ZADANIE 3 - MOBILNY KALENDARZ WEEIA

## Details

The API generates (for the current or selected month) a calendar in ICS/iCal format for data from `http://www.weeia.p.lodz.pl`

## Endpoints

### Request

`GET /events`

### Response

iCalendar file containing events from actual month

### Request

`GET /events/<year>/<month>`

- `<year>` is numeric value relates to year of selected month
- `<month>` is numeric value relates to selected month

### Response

iCalendar file containing events from selected month

## Example

### Request

`GET /events/2020/03`

### Response

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DTSTART;VALUE=DATE:20201008
SUMMARY:Wielka Integracja WIP
UID:8bc86657-67e2-4047-b80c-ac5968452795@8bc8.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20201009
SUMMARY:Wielka Integracja WIP
UID:e93fc064-070d-4e5d-92dc-c32f74c0105a@e93f.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20201010
SUMMARY:Wielka Integracja WIP
UID:3887da7f-9cab-48a9-8b40-e3a0d5a9ca27@3887.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20201001
SUMMARY:Akcja Integracja Online
UID:3bd6e62a-92a9-4990-93f5-b584364b50b5@3bd6.org
URL:https://facebook.com/events/s/akcja-integracja-odkryj-z-nami/3041545625959235/?ti=as
END:VEVENT
END:VCALENDAR
```
