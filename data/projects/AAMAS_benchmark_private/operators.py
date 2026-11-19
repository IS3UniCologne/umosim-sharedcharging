"""Operator configuration."""

from __future__ import annotations

from simulation.helper.configuration.configuration import (
    ChargingInfrastructureConfig,
    RideHailingAllocationEngineConfig,
    RideHailingMPChargingOperationsConfig,
    RideHailingFleetConfig,
    RideHailingOperatorConfig,
    RideHailingSearchEngineConfig,
    RideHailingVehicleConfig,
    VehicleCostConfig,
)
from simulation.helper.enums import AutonomyType, PropulsionType, VehicleType

from simulation.operator.operations_management.ridehailing_MP_charging_operations import(
    RideHailingMPChargingOperations,
)
from simulation.operator.operations_management.algorithms.charging_station_allocation import(
    DowntimeMinWithoutLookahead,
)
from simulation.operator.ride_hailing_allocation_engine import (
    RideHailingAllocationEngine,
)
from simulation.operator.ride_hailing_fleet import RideHailingFleet
from simulation.operator.ride_hailing_search_engine import RideHailingSearchEngine


rh_car_autonomous = RideHailingVehicleConfig(
    VELOCITY_KMH=32.16,
    MAX_AVAILABLE_SEATS=4,
    VEHICLE_TYPE=VehicleType.CAR,
    AUTONOMY_TYPE=AutonomyType.AUTONOMOUS,
    PROPULSION_TYPE=PropulsionType.BATTERY_ELECTRIC,
    ENERGY_CAPACITY=50.0,
    ENERGY_CONSUMPTION_PER_KM=0.20,
    ENERGY_RESERVE_RATIO=0.05,
    PRICE_PER_MIN=0.35,
    PRICE_PER_KM=1.3,
    INITIAL_CHARGE_RATIO=0.50,
    COST_CONFIG=VehicleCostConfig(PER_KM=0.45, DAILY=29.0),
)

RH_AVAILABILITY = [
    0.084238,
    0.058132,
    0.035717,
    0.024728,
    0.027128,
    0.043823,
    0.078576,
    0.128257,
    0.176352,
    0.214981,
    0.241122,
    0.255754,
    0.275117,
    0.293370,
    0.306846,
    0.318127,
    0.323715,
    0.326972,
    0.318448,
    0.290888,
    0.242649,
    0.187925,
    0.142973,
    0.111224,
]

DEFAULT_RECHARGE_THRESHOLD = [
    0.32,
    0.36,
    0.40,
    0.44,
    0.42,
    0.40,
    0.38,
    0.36,
    0.36,
    0.34,
    0.32,
    0.32,
    0.32,
    0.32,
    0.32,
    0.30,
    0.28,
    0.26,
    0.24,
    0.24,
    0.22,
    0.24,
    0.26,
    0.28
]


RH_STATION_HEXES = ["872664c1effffff", "872664c1affffff", "87275934effffff", "872664ca9ffffff", "872664521ffffff", "872664cf5ffffff", "872664cacffffff", "872664c10ffffff", "872664d89ffffff"]


# AAMAS benchmark template: 2 rh operators, both each share half of the charging stations
# meaning each operator "owns" half of the capacity


OPERATORS = [
    RideHailingOperatorConfig(
        FLEET_CONFIG=RideHailingFleetConfig(
            FLEET_TYPE=RideHailingFleet,
            VEHICLES={rh_car_autonomous: 500}, # originally in AAMAS_template 500 AVs
            RH_AVAILABILITY=RH_AVAILABILITY,
            SHIFT_CHECK_INTERVAL_MIN=15,
        ),
        CHARGING_INFRASTRUCTURE=ChargingInfrastructureConfig(
            NUMBER_OF_CHARGING_STATIONS=len(RH_STATION_HEXES),
            LOCATIONS=RH_STATION_HEXES,
            CHARGING_STATION_POWER=[22.0],
            CHARGING_STATION_CAPACITY=[5], # half of the capacity
            CHARGING_STATION_QUEUE_SIZE=[0],
            CHARGING_STATION_PRICE_PROFILE=[0.43] * 24,
        ),
        OPERATIONS_CONFIG=RideHailingMPChargingOperationsConfig(
            OPERATIONS_TYPE=RideHailingMPChargingOperations,
            CHARGING_ALGORITHM_TYPE=DowntimeMinWithoutLookahead,
            OPERATIONS_START=10,
            OPERATIONS_DURATION=50,
            TIME_BETWEEN_OPERATIONS=10,
            RECHARGE_THRESHOLD=DEFAULT_RECHARGE_THRESHOLD,
            VEHICLE_RELOCATION_VELOCITY=32.16,
            LOW_SOC_PENALTY=500_000,
        ),
        SEARCH_ENGINE_CONFIG=RideHailingSearchEngineConfig(
            SEARCH_ENGINE_TYPE=RideHailingSearchEngine,
            AV_PRICE_REDUCTION=0.90,
            MAX_PICKUP_DISTANCE=10000,
            ARRIVAL_LOOKAHEAD_MIN=5,
            PRICE_ENTERING=2.0,
            PRICE_PER_MINUTE=0.35,
            PRICE_PER_KM=1.3,
            MINIMUM_PRICE=5.0,
        ),
        ALLOCATION_ENGINE_CONFIG=RideHailingAllocationEngineConfig(
            VEHICLE_ALLOCATION_ENGINE_TYPE=RideHailingAllocationEngine
        ),

    ),
    RideHailingOperatorConfig(
            FLEET_CONFIG=RideHailingFleetConfig(
                FLEET_TYPE=RideHailingFleet,
                VEHICLES={rh_car_autonomous: 500}, # originally in AAMAS_template 500 AVs
                RH_AVAILABILITY=RH_AVAILABILITY,
                SHIFT_CHECK_INTERVAL_MIN=15,
            ),
            CHARGING_INFRASTRUCTURE=ChargingInfrastructureConfig(
                NUMBER_OF_CHARGING_STATIONS=len(RH_STATION_HEXES),
                LOCATIONS=RH_STATION_HEXES,
                CHARGING_STATION_POWER=[22.0],
                CHARGING_STATION_CAPACITY=[5],# half of the capacity
                CHARGING_STATION_QUEUE_SIZE=[0],
                CHARGING_STATION_PRICE_PROFILE=[0.43] * 24,
            ),
            OPERATIONS_CONFIG=RideHailingMPChargingOperationsConfig(
                OPERATIONS_TYPE=RideHailingMPChargingOperations,
                CHARGING_ALGORITHM_TYPE=DowntimeMinWithoutLookahead,
                OPERATIONS_START=10,
                OPERATIONS_DURATION=50,
                TIME_BETWEEN_OPERATIONS=10,
                RECHARGE_THRESHOLD=DEFAULT_RECHARGE_THRESHOLD,
                VEHICLE_RELOCATION_VELOCITY=32.16,
                LOW_SOC_PENALTY=500_000,
            ),
            SEARCH_ENGINE_CONFIG=RideHailingSearchEngineConfig(
                SEARCH_ENGINE_TYPE=RideHailingSearchEngine,
                AV_PRICE_REDUCTION=0.90,
                MAX_PICKUP_DISTANCE=10000,
                ARRIVAL_LOOKAHEAD_MIN=5,
                PRICE_ENTERING=2.0,
                PRICE_PER_MINUTE=0.35,
                PRICE_PER_KM=1.3,
                MINIMUM_PRICE=5.0,
            ),
            ALLOCATION_ENGINE_CONFIG=RideHailingAllocationEngineConfig(
                VEHICLE_ALLOCATION_ENGINE_TYPE=RideHailingAllocationEngine
            ),
        ),
]
