
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

	
	select rp.name, sum(po.amount_total) total, count(rp.name) compras
	from purchase_order po 
	join res_partner rp on rp.id=po.partner_id 
	group by rp.name
	order by total,compras
	

	
	
	
select * from product_template pt 
select * from product_product pp 


