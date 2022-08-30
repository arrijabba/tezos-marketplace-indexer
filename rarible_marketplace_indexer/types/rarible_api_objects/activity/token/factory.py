from rarible_marketplace_indexer.models import ActivityTypeEnum
from rarible_marketplace_indexer.models import TokenTransfer
from rarible_marketplace_indexer.prometheus.rarible_metrics import RaribleMetrics
from rarible_marketplace_indexer.types.rarible_api_objects.activity.token.activity import BaseRaribleApiTokenActivity
from rarible_marketplace_indexer.types.rarible_api_objects.activity.token.activity import RaribleApiTokenBurnActivity
from rarible_marketplace_indexer.types.rarible_api_objects.activity.token.activity import RaribleApiTokenMintActivity
from rarible_marketplace_indexer.types.rarible_api_objects.activity.token.activity import RaribleApiTokenTransferActivity
from rarible_marketplace_indexer.types.tezos_objects.asset_value.asset_value import AssetValue
from rarible_marketplace_indexer.types.tezos_objects.tezos_object_hash import OriginatedAccountAddress


class RaribleApiTokenActivityFactory:
    @classmethod
    def _build_base_activity(cls, transfer: TokenTransfer) -> BaseRaribleApiTokenActivity:
        try:
            value = AssetValue(transfer.amount)
        except TypeError:
            value = AssetValue(0)

        return BaseRaribleApiTokenActivity(
            transfer_id=transfer.id,
            contract=OriginatedAccountAddress(transfer.contract),
            token_id=transfer.token_id,
            value=value,
            transaction_id=transfer.tzkt_transaction_id,
            date=transfer.date,
        )

    @classmethod
    def build_mint_activity(cls, transfer: TokenTransfer) -> RaribleApiTokenMintActivity:
        base = cls._build_base_activity(transfer)
        if RaribleMetrics.enabled is True:
            RaribleMetrics.set_token_activity(ActivityTypeEnum.TOKEN_MINT, transfer.contract, 1)
        return RaribleApiTokenMintActivity(
            type=ActivityTypeEnum.TOKEN_MINT,
            owner=transfer.to_address,
            **base.dict(),
        )

    @classmethod
    def build_transfer_activity(cls, transfer: TokenTransfer) -> RaribleApiTokenTransferActivity:
        base = cls._build_base_activity(transfer)
        if RaribleMetrics.enabled is True:
            RaribleMetrics.set_token_activity(ActivityTypeEnum.TOKEN_TRANSFER, transfer.contract, 1)
        return RaribleApiTokenTransferActivity(
            type=ActivityTypeEnum.TOKEN_TRANSFER,
            transfer_from=transfer.from_address,
            owner=transfer.to_address,
            **base.dict(),
        )

    @classmethod
    def build_burn_activity(cls, transfer: TokenTransfer) -> RaribleApiTokenBurnActivity:
        base = cls._build_base_activity(transfer)
        if RaribleMetrics.enabled is True:
            RaribleMetrics.set_token_activity(ActivityTypeEnum.TOKEN_BURN, transfer.contract, 1)
        return RaribleApiTokenBurnActivity(
            type=ActivityTypeEnum.TOKEN_BURN,
            owner=transfer.from_address,
            **base.dict(),
        )
