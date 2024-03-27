import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const roomSizes = [19, 20, 34];
  const rooms = roomSizes.map((size) => new ClassRoom(size));
  return rooms;
}
