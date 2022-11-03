--delete from marketplace_order where platform = 'RARIBLE_V1';
--delete from marketplace_activity where platform = 'RARIBLE_V1';
--delete from legacy_orders;
--delete from dipdup_index where name = 'rarible_exchange_legacy_actions';
--delete from dipdup_index where name = 'rarible_exchange_legacy_data_actions';
--delete from indexing_status where index = 'LEGACY_ORDERS';
--delete from indexing_status where index = 'V1_CLEANING';


-- delete from marketplace_order where platform = 'RARIBLE_V2';
-- delete from marketplace_activity where platform = 'RARIBLE_V2';

-- delete from marketplace_order where platform = 'TEIA_V1';
-- delete from marketplace_activity where platform = 'TEIA_V1';

-- delete from marketplace_order where platform = 'FXHASH_V2';
-- delete from marketplace_activity where platform = 'FXHASH_V2';

delete from marketplace_order where platform = 'OBJKT_V2';
delete from marketplace_activity where platform = 'OBJKT_V2';

-- delete from dipdup_index where name = 'fxhash_v1_actions';
-- delete from dipdup_index where name = 'fxhash_v2_actions';
-- delete from dipdup_index where name = 'hen_actions';
-- delete from dipdup_index where name = 'objkt_v1_actions';
delete from dipdup_index where name = 'objkt_v2_actions';
-- delete from dipdup_index where name = 'rarible_exchange_actions';
-- delete from dipdup_index where name = 'rarible_exchange_legacy_actions';
-- delete from dipdup_index where name = 'rarible_exchange_legacy_data_actions';
-- delete from dipdup_index where name = 'teia_v1_actions';
-- delete from dipdup_index where name = 'versum';
-- delete from indexing_status where index = 'LEGACY_ORDERS';
-- delete from indexing_status where index = 'V1_CLEANING';
-- delete from indexing_status where index = 'V1_FILL_FIX';
-- delete from marketplace_order;
-- delete from marketplace_activity;
-- delete from legacy_orders;