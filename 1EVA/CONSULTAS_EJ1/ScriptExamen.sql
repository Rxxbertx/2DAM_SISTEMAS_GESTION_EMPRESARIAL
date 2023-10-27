

--eje3

SELECT * FROM obtener_impuestos_recentes();

--eje4

SELECT * FROM obtener_productos_recentes(); 


--eje7

select po.id , round(po.amount_total,2)  from pos_order po
limit 5

--eje8

select
	rp."name",
	round(sum(po.amount_total),
	2) as gastoTotal
from
	res_partner rp
join pos_order po on
	rp.id = po.partner_id
group by
	rp."name"
order by
	gastoTotal desc
limit 3

--eje9
select
	pt.id,
	pt."name"->>'es_ES' as "name"
from
	product_template pt
where
	pt.id not in (
	select
		pp.product_tmpl_id
	from
		product_product pp,
		pos_order_line pol
	where
		pp.id = pol.product_id)


		
