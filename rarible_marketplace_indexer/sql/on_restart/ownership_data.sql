ALTER TABLE public.ownership DROP CONSTRAINT IF EXISTS ownership_id;
ALTER TABLE public.ownership ADD CONSTRAINT ownership_id UNIQUE (contract, token_id, owner);