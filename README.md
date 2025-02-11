# ISOD iOS notifier

Aplikacja sprawdzająca nowe ogłoszenia z wirtualnego dziekanatu ISOD i wysyłająca powiadomienia na urządzenia iOS przez Pushcut.

## Funkcje

- Automatyczne sprawdzanie nowych ogłoszeń (domyślnie co 60 sekund)
- Możliwość konfiguracji treści powiadomień. Są dostępne dwa typy powiadomień.
  - Pierwsze z tekstem skonfigurowanym w aplikacji. (NOTIFICATION_CONTENT=0)
  - Drugie z tekstem najnowszego powiadomienia. (NOTIFICATION_CONTENT=1)

## Wymagania wstępne

- Docker **lub** Python 3.10+
- Dane dostępowe do API ISOD
- Aplikacja [Pushcut](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://apps.apple.com/us/app/pushcut-shortcuts-automation/id1450936447&ved=2ahUKEwjD_P_KoLyLAxXbKhAIHVM6LHIQFnoECA4QAQ&usg=AOvVaw3vhz_OhbAWoGfCVOvNRlmn)

## Konfiguracja

1. Utwórz plik `.env` z następującymi zmiennymi:

```env
ISOD_API_KEY=twój_klucz_api_isod
ISOD_USERNAME=twój_login_isod
PUSHCUT_API_KEY=twój_klucz_api_pushcut
PUSHCUT_NOTIFICATION_NAME=nazwa_twojego_powiadomienia
CHECK_INTERVAL=60 // Odstęp pomiędzy zapytaniami do isod (w sekundach)
NOTIFICATION_CONTENT=1
```

Klucz isod można wygenerować w isod na dole [swojego profilu](https://isod.ee.pw.edu.pl/isod-stud/person).

### Konfiguracja Pushcut

1. W aplikacji Pushcut naley wygenerować klucz (Account -> Add API Key).
2. W aplikacji Pushcut należy dodać nowe powiadomienie (Notifications -> ikona "+" w prawym górnym rogu). Nazwa tego powiadomienia musi być w .env

## Uruchamianie z Docker'em

1. Zbuduj obraz:

```bash
docker build -t isod-notifier .
```

2. Uruchom kontener:

```bash
docker run -d --env-file .env isod-notifier
```

Aplikacja działa ciągle w tle gdy kontener jest aktywny

## Uruchamianie bez Docker'a

1. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

2. Uruchom aplikację:

```bash
python main.py
```
