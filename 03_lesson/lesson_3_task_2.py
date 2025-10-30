from smartphone import Smartphone

catalog = [
    Smartphone('Iphone', '17 Pro Max', '+79263634888' ),
    Smartphone('Samsung', 'S26', '+79995566444'),
    Smartphone('Google', 'Pixel 7 Pro', '+75556699777'),
    Smartphone('Xiaomi', 'Redmi Note 12 Pro', '+79164556687'),
    Smartphone('OnePlus', 'OnePlus 11', '+79634778956')
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")