# Obsługa błędów
### Projekt grupy: IZ06IO1
### Autorzy: Krzysztof Zerman i Maciej Jakubowski

#### Treść i zakres projektu
```
Aplikacja służąca do zgłaszania problemów z działającym systemem. Do zgłoszenia potrzebny jest
nazwa problemu, krótki opis problemu, osoba wybrana z listy do jego rozwiązania, czas zgłoszenia,
status (zgłoszony, w przetwarzaniu, przekierowany, rozwiązany, zamknięty). Opisy problemów
umieszczane są w bazie utrzymywanej przez serwer. Po otrzymaniu zgłoszenia serwer zawiadamia
za pomocą poczty użytkowników, którzy powinni zająć się problemem. Zwykły użytkownik może
zgłaszać problemy, zmieniać status (oprócz zamykania), przeglądać bazę. Każda zmiana statusu
wymaga wprowadzania komentarza. Główny użytkownik może przeglądać bazę problemów,
przekierowywać problemy, zamykać. Przykład: patrz bugzilla. 
```
## Etapy projektu
* Podstawowa komunikacja klient-server
* Zaimplemetować wysyłanie przez klienta requestu do servera z Nazwą, krótkim opisem, Osobą (wybieraną z listy, server musi zwracać osoby), czasem zgłoszenia, statusem, opisem.
* Zaimplemetować wysyłanie przez server response do klienta z Nazwą, krótkim opisem, Osobą (wybieraną z listy, server musi zwracać osoby), czasem zgłoszenia, statusem, opisem.
* Stworzyć UX dla klienta
* Odbieranie listę błędów z servera dla klienta
* Wysyłanie listy błędów z servera

## W projekcie użyto
* C++ - Serwera
* Python - Klient
