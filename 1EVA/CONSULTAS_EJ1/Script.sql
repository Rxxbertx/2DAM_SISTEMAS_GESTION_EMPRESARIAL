
/*Ejercicio 1: Consulta Básica de Productos y Sus Variantes

Descripción: Identificar todos los productos en product_template y contar cuántas variantes tiene cada uno de ellos en product_product.

Instrucción: Escribe una consulta SQL que muestre el nombre del producto y el número total de variantes que tiene.
*/


select
	pt.id,
	pt.name->>'es_ES',
	count(pt.id)
from
	product_template pt,
	product_product pp
where
	PT.id = PP.product_tmpl_id
group by
	pt.id,
	pt."name"


/*
 * 
 * Ejercicio 2: Pedidos de Venta y Detalle del Cliente

Descripción: Para cada pedido de venta en sale_order, recuperar el nombre del cliente y el total del pedido.

Instrucción: Escribe una consulta SQL que muestre el nombre del cliente (de res_partner) y el total del pedido (de sale_order).

 * 
 * 
 */



select
	so.id as pedido,
	rp.name as costumer,
	so.amount_total as eureles
from
	res_partner rp
join sale_order so on
	rp.id = so.partner_id
where
	rp.id is not null


/*
 * Ejercicio 3: Total de Órdenes PoS por Cliente

Descripción: Calcula el total de órdenes realizadas a través del Punto de Venta (PoS) por cada cliente.

Instrucción:
Escribe una consulta SQL que muestre el nombre del cliente y el total de órdenes PoS que ha realizado.
 */


select
	rp.name,
	count(rp.id) as compras
from
	pos_order po
join res_partner rp on
	po.partner_id = rp.id
group by
	rp.name

	
	/*
	 * Ejercicio 4: Detalle de Producto más Vendido en PoS

Descripción: Identifica el producto que ha sido más vendido a través del Punto de Venta y muestra su nombre y la cantidad total vendida.

Instrucción:
Escribe una consulta SQL que muestre el nombre del producto más vendido y la cantidad total vendida de ese producto a través de las transacciones PoS
	 */
	
	
	
select
	pol.full_product_name ,
	sum(pol.qty)
from
	pos_order_line pol
group by
	pol.full_product_name

	

select
	pt.name->>'es_ES' as product_name,
	sum(qty)
from
	pos_order_line pol ,
	product_template pt ,
	product_product pp
where
	pt.id = pp.product_tmpl_id
	and
	pol.product_id = pp.id
group by
	pt."name"
order by
	sum(qty) desc


/*
 * Ejercicio 5: Proveedores y Total de Órdenes de Compra

Descripción: Obtén una lista de todos los proveedores y calcula el total de órdenes de compra que se les ha hecho.

Instrucción:
Escribe una consulta SQL que muestre el nombre del proveedor y el número total de órdenes de compra relacionadas con él.
 */

select
	rp."name" as name,
	count(po.partner_id)
from
	res_partner rp
join purchase_order po on
	po.partner_id = rp.id
group by
	po.partner_id ,
	rp."name"

	
	
/*
 * Ejercicio 6: Productos Vendidos en Punto de Venta con Valor Superior a 1000

Descripción: Encuentra todos los productos que se han vendido a través del Punto de Venta cuyo valor total por transacción excede los 1000.

Instrucción:
Escribe una consulta SQL que muestre el nombre del producto y el valor total de la transacción para aquellos productos cuyas transacciones en el Punto de Venta superan los 1000.
 */	
	
	
select
	pol.full_product_name ,
	po.amount_total
from
	pos_order po
join pos_order_line pol on
	po.id = pol.order_id
where
	po.amount_total > 1000

	/*
	 * Ejercicio 7: Clientes sin Órdenes de Venta

Descripción: Encuentra los clientes que no han realizado ninguna orden de venta.

Instrucción:
Escribe una consulta SQL que muestre los nombres de los clientes que no tienen asociada ninguna orden de venta en sale_order.
	 */

	select
	rp."name"
from
	res_partner rp
left join sale_order so on
	rp.id = so.partner_id
where
	so.partner_id is null
	
	
/*
 * Ejercicio 8: Productos no Vendidos en Punto de Venta

Descripción: Determina qué productos no se han vendido a través del Punto de Venta.

Instrucción:
Escribe una consulta SQL que liste los nombres de los productos que no han sido vendidos a través del Punto de Venta.
 */	
	
select
	pt.name->>'es_ES'
from
	 product_product pp
	 
left join pos_order_line pol on
	pol.product_id = pp.id
	
join product_template pt on
	pt.id = pp.product_tmpl_id

	where
	pol.product_id is null

	/*
	 * Ejercicio 9: Valor Total de Facturas por Cliente

Descripción: Calcula el valor total de todas las facturas por cliente.

Instrucción:
Escribe una consulta SQL que muestre el nombre del cliente y el valor total acumulado de sus facturas.
	 */
	
	
	select
	rp.name as nombre_cliente,
	SUM(am.amount_total) as valor_total_facturas
from
	account_move as am
join
    res_partner as rp on
	am.partner_id = rp.id
where
	am.move_type = 'out_invoice'
	-- Para obtener solo facturas de ventas
group by
	rp.name
    
/*
 * 
 * Ejercicio 10: Productos con Más Variantes Vendidas en Punto de Venta

Descripción: Determina qué producto ha tenido más variantes vendidas en el Punto de Venta.

Instrucción:
Escribe una consulta SQL que muestre el nombre del producto y el número de sus distintas variantes que se han vendido a través del Punto de Venta.
 * 
 */
	
WITH VariantesVendidas AS (
    SELECT
        pt."name" AS nombre_producto,
        pa."name" AS nombre_atributo,
        pav."name" AS nombre_variante,
        pol.qty AS cantidad_ventas
    FROM
        pos_order_line pol
    JOIN
        product_product pp ON pol.product_id = pp.id
    JOIN
        product_template pt ON pt.id = pp.product_tmpl_id
    JOIN
        product_template_attribute_value ptav ON ptav.product_tmpl_id = pt.id
    JOIN
        product_attribute pa ON pa.id = ptav.attribute_id
    JOIN
        product_attribute_value pav ON pav.id = ptav.product_attribute_value_id
    GROUP BY
        pt."name", pa."name", pav."name",pp.id , pol.product_id ,pol.qty
)

SELECT(nombre_producto, nombre_atributo)
    nombre_producto,
    nombre_atributo,
    nombre_variante,
    cantidad_ventas
FROM
    VariantesVendidas
ORDER BY
    nombre_producto, nombre_atributo, cantidad_ventas DESC;




