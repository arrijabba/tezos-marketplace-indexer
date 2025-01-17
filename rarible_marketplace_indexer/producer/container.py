from __future__ import annotations

from logging import Logger
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from aiokafka import AIOKafkaProducer

from rarible_marketplace_indexer.producer.null_kafka_producer import NullKafkaProducer
from rarible_marketplace_indexer.producer.serializer import kafka_key_serializer
from rarible_marketplace_indexer.producer.serializer import kafka_value_serializer

AIOKafkaProducerInterface = Union[AIOKafkaProducer, NullKafkaProducer]


class ProducerContainer:
    __instance: Optional[AIOKafkaProducerInterface] = None

    @classmethod
    def get_instance(cls) -> AIOKafkaProducerInterface:
        if not isinstance(cls.__instance, AIOKafkaProducerInterface):
            raise RuntimeError
        return cls.__instance

    @classmethod
    def create_instance(cls, config: Dict[str, Any], logger: Logger) -> None:
        if config['enabled'] != 'false':
            if config['kafka_security_protocol'] == 'SASL_PLAINTEXT':
                addresses = [config['kafka_address']]
                logger.info(f"Connecting to kafka using {config['kafka_security_protocol']}: addresses {addresses}")
                producer = AIOKafkaProducer(
                    bootstrap_servers=addresses,
                    client_id=config['client_id'],
                    security_protocol=config['kafka_security_protocol'],
                    sasl_mechanism=config['sasl']['mechanism'],
                    sasl_plain_username=config['sasl']['username'],
                    sasl_plain_password=config['sasl']['password'],
                    value_serializer=kafka_value_serializer,
                    key_serializer=kafka_key_serializer,
                )
            else:
                addresses = config['kafka_address'].split(',')
                logger.info(f"Connecting to internal kafka: {addresses}")
                producer = AIOKafkaProducer(
                    bootstrap_servers=addresses,
                    client_id=config['client_id'],
                    sasl_mechanism=config['sasl']['mechanism'],
                    value_serializer=kafka_value_serializer,
                    key_serializer=kafka_key_serializer,
                )
        else:
            producer = NullKafkaProducer()

        cls.__instance = producer
