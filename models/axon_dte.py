# -*- coding: utf-8 -*-

import requests
import json
import logging
import os

class Axon:

    def genBoleta(order, respuesta):
        NombreLog = "debug"
        ArchLog = NombreLog+".log"
        fichero_log = os.path.join(ArchLog)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', filename=fichero_log, filemode='w', )
        logging.debug("------------------------------")
        logging.debug(str(order))


        dict_boleta = {
            "DATOSCONECT": {
                "Usuario": "axondte",
                "Clave": "axondte"
            },
            "DATOSEMP": {
                "Rut_emisor": "96901560-9",
                "Tipo_doc": 39,
                "Accion": "GENDTE"
            },
            "RECEPTOR": {
                "Rut_cliente": "xxxxxxxxx-x",
                "Nombre_cliente": "",
                "Direccion": "",
                "Comuna": "",
                "Ciudad": "",
                "Correo_enviaPDF": "  "
            },
            "REG001": {
                "Campo12": 39,
                "Campo13": "0000000000",
                "Campo14": "2020-06-15",
                "Campo15": 3,
                "Campo20": "96901560-9",
                "Campo21": "AXON SOFTWARE SPA",
                "Campo22": "ARRIENDO Y VENTA DE SOFTWARE",
                "Campo23": "00000000",
                "Campo24": " ",
                "Campo26": " ",
                "Campo27": "66666666-6",
                "Campo28": " ",
                "Campo29": " ",
                "Campo30": " ",
                "Campo31": " ",
                "Campo32": " ",
                "Campo33": " ",
                "Campo34": " ",
                "Campo35": " ",
                "Campo36": " ",
                "Campo40": "0000040700",
                "Campo41": " ",
                "Campo42": " ",
                "Campo43": " ",
                "Campo44": " "
            },
            "REG002": [{
                    "Campo45": "0001",
                    "Campo46": "interna",
                    "Campo47": "0000000000321",
                    "Campo50": "96901560-9",
                    "Campo51": "PROMO CEVICHE PISCO SUOR",
                    "Campo63": "000000000001.000000",
                    "Campo65": "0000000000012900.00",
                    "Campo70": "000000012900"
                },
                {
                    "Campo45": "0002",
                    "Campo46": "interna",
                    "Campo47": "0000000000005",
                    "Campo50": "96901560-9",
                    "Campo51": "MIX DE CEVICHES",
                    "Campo63": "000000000001.000000",
                    "Campo65": "0000000000014900.00",
                    "Campo70": "000000014900"
                },
                {
                    "Campo45": "0003",
                    "Campo46": "interna",
                    "Campo47": "0000000000006",
                    "Campo50": "96901560-9",
                    "Campo51": "JALEA NORTENA",
                    "Campo63": "000000000001.000000",
                    "Campo65": "0000000000012900.00",
                    "Campo70": "000000012900"
                }
            ],
            "REGTOTALES": {
                "Sub_total": "0000040700",
                "Descuento_global": "0000000000",
                "Total": "0000040700",
                "Total_pagos": "0000040700",
                "Vuelto": "0000000000"
            },
            "REGPAGOS": [{
                    "Nombre_mdp": "Efectivo",
                    "Monto_pago": "0000020700"
                },
                {
                    "Nombre_mdp": "Tarjeta de Debito",
                    "Monto_pago": "0000010000"
                },
                {
                    "Nombre_mdp": "Tarjeta de Credito",
                    "Monto_pago": "0000010700"
                }
            ],
            "COMENTARIO": {
                "Comentario": "Comentario al pie de pagina"
            }
        }

        strBoleta = json.dumps(dict_boleta)
        print(strBoleta)
        try:
            req = requests.get('http://191.235.103.59:8888/integdte/'+strBoleta)
            print(req.status_code)
        except:
            print('Error llamada API GEN DTE')

        logging.DEBUG('voy a imprimir la orden')
        logging.DEBUG(str(json.dumps(order)))
        logging.DEBUG('ya imprimi la orden')
        #logging.info(str(respuesta))


        return req

    #genBoleta()

    """
        #DATOS CONNECT
        Usuario = 'axondte'
        Clave = 'axondte'
        
        #DATOSEMP
        Rut_emisor = '96901560-9'
        Tipo_doc = 39
        Accion = 'GENDTE'
        
        #RECEPTOR
        Rut_cliente = ''
        Nombre_cliente = 'PABLO BECERRA'
        Direccion = 'CARMEN 8, PISO 8'
        Comuna = 'SANTIAGO'
        Ciudad = 'SANTIAGO'
        Correo_enviaPDF = 'pablo@axonsoftware.cl'
        
        #REG001
        Campo12 = Tipo_doc # Tipo de documento
        Campo13 = '0000000000' # Folio del documento
        Campo14 = '2020-06-15' #Fecha de emision del documento
        Campo15 = 3 # Indicador de servicio
        Campo20 = Rut_emisor # Rut del emisor
        Campo21 = 'AXON SOFTWARE SPA' # Razon social del emisor
        Campo22 = 'ARRIENDO Y VENTA DE SOFTWARE' # Giro del emisor
        Campo23 = '00000000' # Codigo sucursal SII
        Campo24 = '' # Dirección de origen
        Campo26 = '' # Ciudad de la sucursal de origen
        Campo27 = '66666666-6' # Rut del receptor
        Campo28 = '' # Código interno del cliente
        Campo29 = '' # Nombre del receptor
        Campo30 = '' # Contacto del receptor
        Campo31 = '' # Direccion del receptor
        Campo32 = '' # Comuna del receptor
        Campo33 = '' # Ciudad del receptor
        Campo34 = '' # Dirección postal
        Campo35 = '' # Comuna postal
        Campo36 = '' # Ciudad postal
        Campo40 = '0000040700' # Monto total
        Campo41 = '' # Monto no facturable
        Campo42 = '' # Total período
        Campo43 = '' # Saldo anterior
        Campo44 = '' # Valor a pagar

        #REG002
        Campo45 = '0001' # Numero secuencial de linea
        Campo46 = 'interna' # Tipo de codificación utilizada
        Campo47 = '0000000000321' # Código del producto
        Campo50 = Rut_emisor # RUT de la empresa mandante de la boleta
        Campo51 = 'PROMO CEVICHE PISCO SOUR' # Nombre del producto o servicio
        Campo63 = '000000000001.000000' # Cantidad
        Campo65 = '0000000000012900.00' # Precio unitario
        Campo70 = '000000012900' # Valor por línea de detalle (cantidad * precio)
        
        #REGTOTALES
        Sub_total = '0000040700'
        Descuento_global = '0000000000'
        Total = '0000040700'
        Total_pagos = '0000040700'
        Vuelto = '0000000000'
        
        #REGPAGOS
        Nombre_mdp = 'Efectivo'
        Monto_pago = '0000020700'
        
        #COMENTARIO
        Comentario = 'Comentario al pie de pagina'
    """
























"""
{'data':
          {'amount_paid': untax + atax,
           'amount_return': 0,
           'amount_tax': atax,
           'amount_total': untax + atax,
           'creation_date': fields.Datetime.to_string(fields.Datetime.now()),
           'fiscal_position_id': False,
           'pricelist_id': self.pos_config.available_pricelist_ids[0].id,
           'lines': [[0,
             0,
             {'discount': 0,
              'id': 3,
              'pack_lot_ids': [],
              'price_unit': 1.2,
              'product_id': self.whiteboard_pen.id,
              'price_subtotal': 1.2,
              'price_subtotal_incl': 1.38,
              'qty': 1,
              'tax_ids': [(6, 0, self.whiteboard_pen.taxes_id.ids)]}]],
           'name': 'Order 00043-003-0014',
           'partner_id': False,
           'pos_session_id': current_session.id,
           'sequence_number': self.pos_config.journal_id.id,
           'statement_ids': [[0,
             0,
             {'amount': untax + atax,
              'name': fields.Datetime.now(),
              'payment_method_id': self.credit_payment_method.id}]],
           'uid': '00043-003-0014',
           'user_id': self.env.uid},
          'id': '00043-003-0014',
          'to_invoice': False}
"""