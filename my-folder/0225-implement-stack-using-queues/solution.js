class MyQueue {
    constructor() { 
        this.data = [];
        this.front = 0;
        this.rear = 0;
    }
    
    // Add the 'element' to the rear of the queue
    // Time: O(1)
    enqueue(element) {
        this.data[this.rear] = element;
        this.rear++;
    }
    
    isEmpty() {
        return this.front == this.rear;
    }
    
    print() {
        for(let i = this.front; i < this.rear; ++i)
            console.log(this.data[i]);
    }
    
    // Delete the front element and return the deleted element
    // Time: O(1)
    dequeue() {
        if(this.isEmpty()) {
            throw new Error("Queue Underflow");
        }
        let frontElement = this.data[this.front];
        this.front++;
        return frontElement;
    }
    
    length() {
        return this.rear - this.front;    
    }
    
    // Just return the front element
    // Time: O(1)
    getFront() {
        if(this.isEmpty()) {
            throw new Error("Queue is Empty!");
        }
        return this.data[this.front];
    }
}

var MyStack = function() {
    this.q1 = new MyQueue();
    this.q2 = new MyQueue();
    this.length = 0; 
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    this.q1.enqueue(x);
    this.length++;
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    // Transfer N - 1 elements from Q1 to Q2.
    for(let i = 0; i < this.length - 1; i++)
        this.q2.enqueue(this.q1.dequeue());

    // Delete the last remaining element.
    let poppedElement = this.q1.dequeue();

    // Transfer back the elements from Q2 to Q1.
    while(!this.q2.isEmpty())
        this.q1.enqueue(this.q2.dequeue());

    // Decrement length by 1
    this.length--;

    return poppedElement;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    // Transfer N - 1 elements from Q1 to Q2.
    for(let i = 0; i < this.length - 1; i++)
        this.q2.enqueue(this.q1.dequeue());

    // Get the last remaining element.
    let topElement = this.q1.dequeue();

    // Transfer back the elements from Q2 to Q1.
    while(!this.q2.isEmpty())
        this.q1.enqueue(this.q2.dequeue());

    // Enqueue the last remaining element again.
    this.q1.enqueue(topElement);

    return topElement;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.length == 0;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
