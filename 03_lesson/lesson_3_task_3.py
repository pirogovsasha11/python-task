from address import Address
from mailing import Mailing

recipient = Address(142613, 'Москва', 'Наумова', 36, 255)

sender= Address(163345, 'Сочи', 'Герасимова', 14, 136 )

parcel = Mailing(to_address = recipient, from_address = sender, cost = 3000, track = 'POST123456789')

print(f"Отправление {parcel.track} из {parcel.from_address.index}, {parcel.from_address.city}, {parcel.from_address.street}, {parcel.from_address.house} - {parcel.from_address.apartment} "
      f"в {parcel.to_address.index}, {parcel.to_address.city}, {parcel.to_address.street}, {parcel.to_address.house} - {parcel.to_address.apartment}. "
      f"Стоимость {parcel.cost} рублей.")