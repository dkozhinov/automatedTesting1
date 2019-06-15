Feature: Testing site cbr.ru
Scenario: Search Bank of Russia site on google.ru
  Given website www.google.ru
  When push search button with text 'Центральный банк РФ'
  Then displayed page www.google.ru and opened link 'https://www.cbr.ru/'
  Then on cbr.ru opened link Internet-reception
  Then on cbr.ru opened link Write gratitude
  Then on cbr.ru write gratitude on textarea MessageBody 'случайный текст'