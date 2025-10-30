from smartphone import Smartphone

catalog = [
    Smartphone('Iphone', '17 Pro Max', '8(926)36-34-888' ),
    Smartphone('Samsung', 'S26', '8(999)55-66-444'),
    Smartphone('Google', 'Pixel 7 Pro', '8(555)66-99-777'),
    Smartphone('Xiaomi', 'Redmi Note 12 Pro', '8(916)45-56-687'),
    Smartphone('OnePlus', 'OnePlus 11', '8(963)47-78-956')
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")