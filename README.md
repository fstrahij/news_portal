# news_portal
Ovaj projekt u backendu dohvaća 4 rss kanala (news, show, sport i tech) na 24sata.hr te ih parsira i nakon toga sprema u modele Channel i Article. Za dohvat, parsiranje i spremanje kanala u bazu se koristi naredba:
 - <b> manage.py parserss </b>

Sljedeći je dio u kojem se pokreće server. Serializirani podaci iz modela se prikazuju u rest api endpointu i mogu se vidjeti na: 
 - <b> https://localhost:[broj_porta]/api/ </b>

Sama aplikacija se nalazi na localhostu. U aplikaciji je moguće dohvaćati podatake prema odabranom kanalu, pretraživati prema opisu i naslovu te je izrađena jednostavna paginacija. Prikazuje se po 10 članaka na stranici.      
