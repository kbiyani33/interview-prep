from typing import List, Optional
from datetime import datetime

class ParkingManager:
    def __init__(self, manager_id: int) -> None:
        self.manager_id: int = manager_id
        self.parking_lots: List[ParkingLot] = []

    def add_parking_lot(self, parking_lot: 'ParkingLot') -> None:
        self.parking_lots.append(parking_lot)

class ParkingLot:
    def __init__(self, lot_id: int) -> None:
        self.lot_id: int = lot_id
        self.floors: List[ParkingFloor] = []

    def add_floor(self, floor: 'ParkingFloor') -> None:
        self.floors.append(floor)

class ParkingFloor:
    def __init__(self, floor_id: int) -> None:
        self.floor_id: int = floor_id
        self.spots: List[ParkingSpot] = []

    def add_spot(self, spot: 'ParkingSpot') -> None:
        self.spots.append(spot)

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: str) -> None:
        self.spot_id: int = spot_id
        self.spot_type: str = spot_type
        self.is_occupied: bool = False
        self.vehicle: Optional['Vehicle'] = None

    def assign_vehicle(self, vehicle: 'Vehicle') -> None:
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self) -> None:
        self.vehicle = None
        self.is_occupied = False

class Vehicle:
    def __init__(self, vehicle_id: int, vehicle_type: str) -> None:
        self.vehicle_id: int = vehicle_id
        self.vehicle_type: str = vehicle_type
        self.ticket: Optional['Ticket'] = None

    def assign_ticket(self, ticket: 'Ticket') -> None:
        self.ticket = ticket

class Ticket:
    def __init__(self, ticket_id: int, issue_time: datetime, expiry_time: datetime, parking_spot: 'ParkingSpot') -> None:
        self.ticket_id: int = ticket_id
        self.issue_time: datetime = issue_time
        self.expiry_time: datetime = expiry_time
        self.parking_spot: ParkingSpot = parking_spot

    def get_parking_spot(self) -> 'ParkingSpot':
        return self.parking_spot