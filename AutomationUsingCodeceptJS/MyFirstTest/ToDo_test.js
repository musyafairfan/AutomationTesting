Feature('Ayo Nonton Youtube');

Scenario('Goooooooo', ({ I }) => {
  I.resizeWindow(1500, 800)
  I.amOnPage('http://youtube.com/');
  I.wait(3)
  I.fillField('Search', 'Drum cover Tarn Softwhip');
  I.pressKey('Enter');
  I.wait(10)
  I.click('Avenged Sevenfold - Nightmare Drum Cover By Tarn Softwhip female drummer')
  I.wait(6.1);
  I.click('Skip Ads')
  I.click('No thanks')
  I.wait(360)
});