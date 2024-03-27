export default class HolbertonCourse {
    constructor(name, length, students) {
      if (typeof name !== 'string') {
        throw new TypeError('name must be a string');
      }
      this._name = name;
  
      if (typeof length !== 'number') {
        throw new TypeError('length must be a number');
      }
      this._length = length;
  
      if (
        !Array.isArray(students)
        || !students.every((student) => typeof student === 'string')
      ) {
        throw new TypeError('students must be an array');
      }
      this._students = students;
    }
  
    // Getter and setter for name
    get name() {
      return this._name;
    }
  
    set name(newName) {
      if (typeof newName !== 'string') {
        throw new TypeError('name must be a string');
      }
      this._name = newName;
    }
  
    // Getter and setter for length
    get length() {
      return this._length;
    }
  
    set length(newLength) {
      if (typeof newLength !== 'number') {
        throw new TypeError('length must be a number');
      }
      this._length = newLength;
    }
  
    // Getter and setter for students
    get students() {
      return this._students;
    }
  
    set students(newStudents) {
      if (
        !Array.isArray(newStudents)
        || !newStudents.every((student) => typeof student === 'string')
      ) {
        throw new TypeError('students must be an array');
      }
      this._students = newStudents;
    }
  }
