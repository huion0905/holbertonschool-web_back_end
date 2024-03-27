export default class Building {
    constructor(sqft) {
      if (typeof sqft !== 'number') {
        throw new TypeError('sqft must be a number');
      }
      this._sqft = sqft;
  
      if (this.constructor !== Building) {
        this.evacuationWarningMessage();
      }
    }
  
    // Getter and setter for sqft
    get sqft() {
      return this._sqft;
    }
  
    set sqft(newValue) {
      if (typeof newValue !== 'number') {
        throw new TypeError('sqft must be a number');
      }
      this._sqft = newValue;
    }
  
    // eslint-disable-next-line class-methods-use-this
    evacuationWarningMessage() {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
  }
