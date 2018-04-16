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
* Odbieranie listę błędów z serwera dla klienta
* Wysyłanie listy błędów z serwera

## W projekcie użyto
* C++ - Serwera
* Python - Klient

## GitFlow
##### https://datasift.github.io/gitflow/IntroducingGitFlow.html
![alt text](https://datasift.github.io/gitflow/GitFlowDevelopBranch.png)
* Starajmy się w nazwie zawierać czy dany feature branch dotyczy clienta czy serwera, żeby sobie nie wchodzić w drogę ;)
* Nie commitujmy nic od razu na develop a tym bardziej na master
* Jak już skończymy jakiś branch i uznamy, że starczy commitów to wysyłamy kod drugiej osobie do review
* W kliencie i serwerze znajdują się pliki README.md, tam wpisujmy różne ustalenia i ważniejsze rzeczy które chcemy robić w projekcie (tak żeby była jakaś dokumentacja)
