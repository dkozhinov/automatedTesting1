Feature: Testing site cbr.ru
Scenario: Search Bank of Russia site on google.ru
  Given website www.google.ru
  When push search button with text 'Центральный банк РФ'
  Then displayed page www.google.ru and opened link 'https://www.cbr.ru/'
  Then on cbr.ru opened link Internet-reception
  Then opened link Write gratitude
  Then write in textarea MessageBody 'случайный текст'
  Then select the checkbox Agreement
  Then make screenshot and send email