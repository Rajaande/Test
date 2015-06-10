#!/usr/bin/python
import os
import codecs

from xml.dom import minidom

git_urls ={'atos-sips-dev' : 'http://RAnde@stash.ht.powa.com/scm/aim/atos-sips-dev.git',
           'adyen-dev':'http://RAnde@stash.ht.powa.com/scm/aim/adyen-dev.git',
            'authorize-net':'http://RAnde@stash.ht.powa.com/scm/aim/authorize-net.git',
           'atg-dev':'http://RAnde@stash.ht.powa.com/scm/aim/atg-dev.git',
           'barclaycard-epdq-dev':' http://RAnde@stash.ht.powa.com/scm/aim/barclaycard-epdq-dev.git',
           'barclaycard-smartpay-dev':' http://RAnde@stash.ht.powa.com/scm/aim/barclaycard-smartpay-dev.git',
           'braintree-dev':'http://RAnde@stash.ht.powa.com/scm/aim/braintree-dev.git',
           'buckaroo-dev':' http://RAnde@stash.ht.powa.com/scm/aim/buckaroo-dev.git',
           'chase-dev':'http://RAnde@stash.ht.powa.com/scm/aim/chase-dev.git',
           'computop-dev':'http://RAnde@stash.ht.powa.com/scm/aim/computop-dev.git',
           'cybermut-dev':'http://RAnde@stash.ht.powa.com/scm/aim/cybermut-dev.git',
           'cybersource-dev':'http://RAnde@stash.ht.powa.com/scm/aim/cybersource-dev.git',
           'datacash-dev':'http://RAnde@stash.ht.powa.com/scm/aim/datacash-dev.git',
           'dibs-dev':'http://RAnde@stash.ht.powa.com/scm/aim/dibs-dev.git',
           'epay-dev':'http://RAnde@stash.ht.powa.com/scm/aim/epay-dev.git',
           'fetchapp-dev-new':'http://RAnde@stash.ht.powa.com/scm/aim/fetchapp-dev-new.git',
           'firstdata-dev':'http://RAnde@stash.ht.powa.com/scm/aim/firstdata-dev.git',
           'global-collect-dev':'http://RAnde@stash.ht.powa.com/scm/aim/global-collect-dev.git',
            #'gestpay-dev':'http://RAnde@stash.ht.powa.com/scm/aim/gestpay-dev.git',
            'ghd-dev':'http://RAnde@stash.ht.powa.com/scm/aim/ghd-dev.git',
           'hybris-dev':'http://RAnde@stash.ht.powa.com/scm/aim/hybris-dev.git',
           'hipay-dev': 'http://RAnde@stash.ht.powa.com/scm/aim/hipay-dev.git',
           'logic-group-dev': 'http://RAnde@stash.ht.powa.com/scm/aim/logic-group-dev.git',
           'notification-hibernate-dao':'http://RAnde@stash.ht.powa.com/scm/aim/notification-hibernate-dao.git',
           'nopcommerce-dev':'http://RAnde@stash.ht.powa.com/scm/aim/nopcommerce-dev.git',
           'ogone-dev':'http://RAnde@stash.ht.powa.com/scm/aim/ogone-dev.git',
           'optimal-dev':'http://RAnde@stash.ht.powa.com/scm/aim/optimal-dev.git',
           'pay-box-dev':'http://RAnde@stash.ht.powa.com/scm/aim/pay-box-dev.git',
           'payex-dev':'http://RAnde@stash.ht.powa.com/scm/aim/payex-dev.git',
           'paymentsense-dev':'http://RAnde@stash.ht.powa.com/scm/aim/paymentsense-dev.git',
           'payone':'http://RAnde@stash.ht.powa.com/scm/aim/payone.git',
           #'payline-dev':'http://RAnde@stash.ht.powa.com/scm/aim/payline-dev.git',
           'paypal-dev':'http://RAnde@stash.ht.powa.com/scm/aim/paypal-dev.git',
           'paypoint-dev':'http://RAnde@stash.ht.powa.com/scm/aim/paypoint-dev.git',
           'paypoint-rest-dev':'http://RAnde@stash.ht.powa.com/scm/aim/paypoint-rest-dev.git',
           'payzen-dev':'http://RAnde@stash.ht.powa.com/scm/aim/payzen-dev.git',
            'powaaim':'http://RAnde@stash.ht.powa.com/scm/aim/powaaim.git',
           'prestashop-dev':'http://RAnde@stash.ht.powa.com/scm/aim/prestashop-dev.git',
           'realex-dev':'http://RAnde@stash.ht.powa.com/scm/aim/realex-dev.git',
           'redsys-dev':'http://RAnde@stash.ht.powa.com/scm/aim/redsys-dev.git',
           'sagepay-dev':'http://RAnde@stash.ht.powa.com/scm/aim/sagepay-dev.git',
           'scryptdata':'http://RAnde@stash.ht.powa.com/scm/aim/scryptdata.git',
           'securetrading':'http://RAnde@stash.ht.powa.com/scm/aim/securetrading.git',
           'seoshop-dev':'http://RAnde@stash.ht.powa.com/scm/aim/seoshop-dev.git',
           'setefi-dev':'http://RAnde@stash.ht.powa.com/scm/aim/setefi-dev.git',
           'skrill-dev':'http://RAnde@stash.ht.powa.com/scm/aim/skrill-dev.git',
           'stripe-dev':'http://RAnde@stash.ht.powa.com/scm/aim/stripe-dev.git',
           'teller-dev':'http://RAnde@stash.ht.powa.com/scm/aim/teller-dev.git',
           'textalk-dev':'http://RAnde@stash.ht.powa.com/scm/aim/textalk-dev.git',
           # 'tns-dev':'http://RAnde@stash.ht.powa.com/scm/aim/tns-dev.git',
           'verifone-dev':'http://RAnde@stash.ht.powa.com/scm/aim/verifone-dev.git',
           'wepay-dev':'http://RAnde@stash.ht.powa.com/scm/aim/wepay-dev.git',
           'worldpay':'http://RAnde@stash.ht.powa.com/scm/aim/worldpay.git',
           'venda':'http://RAnde@stash.ht.powa.com/scm/aim/venda.git'
}

os.chdir('/usr/local/dev/1.7.0/')
for key in git_urls:
   os.system("git clone "+ git_urls[key])
   os.chdir('/usr/local/dev/1.7.0/'+key)
   os.system('git co develop')
   os.system('git co -b release/1.7.0')
   doc = minidom.parse("pom.xml")

   versions = doc.getElementsByTagName("version")
   for versionList in versions:
      if versionList.parentNode.nodeName == 'project' :
         snapshotVesrion=versionList.firstChild.nodeValue
         versionList.firstChild.nodeValue  = snapshotVesrion.replace("SNAPSHOT","RC-SNAPSHOT")
         f = open("pom.xml", 'w')
         doc.writexml(f)
         f.close()
         os.system('git commit -a -m "POWAAIM-908: craeted release branch from develop"')
         os.system('git push origin release/1.7.0')
         os.chdir('/usr/local/dev/1.7.0')




