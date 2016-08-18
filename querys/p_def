SELECT  id, nome  FROM players where clube_id IN (
select casa from partidas, current_atk  where current_atk.clube_id = partidas.visitante order by ataque ASC LIMIT 6) and
posicao_id = 3  and  status = 7  and jogos_num > 8
order by media_num DESC
limit 1
