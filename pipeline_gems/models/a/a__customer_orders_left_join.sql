{{
  config({    
    "materialized": "ephemeral",
    "database": "prophecy-field",
    "schema": "nadeesh_demos"
  })
}}

WITH orders AS (

  SELECT * 
  
  FROM {{ source('prophecy_field_abhinav_demos', 'orders') }}

),

customers AS (

  SELECT * 
  
  FROM {{ source('prophecy_field_abhinav_demos', 'customers') }}

),

customer_orders_left_join AS (

  {#Lists all customers along with their orders, including those who have not placed any orders.#}
  SELECT 
    in1.customer_id AS customer_id,
    in1.order_id AS order_id
  
  FROM customers AS in0
  LEFT JOIN orders AS in1
     ON in1.customer_id = in0.customer_id

)

SELECT *

FROM customer_orders_left_join
