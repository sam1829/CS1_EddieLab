"""
author: Susan Margevich
file name: myList.py
modified node and slList code
"""

from rit_lib import *
from random import *

"""
Node functions and code
"""
###########################################################
# NODE CLASS DEFINITIONS
###########################################################


class Node( struct ):
    """
       Slots of a linked node structure
       data: an object reference allows any kind of element
       next: either a Node reference or None
    """
    # syntax is rit_object version 2.5b
    _slots = (( object, 'data'),(int, 'landed'), ((NoneType, 'Node'), 'next' ))

def test_node():
    """
    test_node tests the {NoneType, Node} type constructions
    """
    node1 = Node( 'first', None )
    print( node1.data == 'first' and node1.next == None )
    node2 = Node( 'one-two', Node( 'two', None ) )
    print( node2.data == 'one-two' )
    print( isinstance( node2.next, Node ) )
    print( node2.next.data == 'two' )
    print( node2.next.next == None )


if __name__ == "__main__":
    test_node()


"""
slList code and functions
"""

###########################################################
# LINKED LIST CLASS DEFINITION
###########################################################

class SlList( struct ):
    """
    SlList class encapsulates a node based linked list.
    'head' slot refers to a Node instance.
    'size' slot holds the number of nodes in the list.
    """
    _slots = ( ((Node, NoneType), 'head') \
             , (int, 'size' ) \
             , ((Node, NoneType), 'cursor'))


###########################################################
# LINKED LIST CLASS CONSTRUCTOR
###########################################################

def createList():
    """
       Create and return an instance
       of an empty node-based, single-linked list.
       Parameters:
           None
       Returns:
           An empty list
    """
    return SlList( None, 0, None )


###########################################################
# CURSOR FUNCTIONS
###########################################################

def reset(lst):
    """
    Resets the cursor to the start of the list

    Parameters:
        lst (SlList) - the linked list
    Returns:
        None
    """

    lst.cursor = lst.head

def hasNext(lst):
    """
    Returns True if the list has more elements.

    Parameters:
        lst (SlList) - the linked list
    Returns:
        True (bool) if the cursor is value
    """

    return not lst.cursor == None

def next(lst):
    """
    Returns the next element in the iteration.

    Parameters:
        lst (SlList) - the linked list
    Preconditions:
        If cursor is invalid, raises an IndexError exception
    Returns:
        The value (any type) referenced by the cursor
    """

    if lst.cursor == None :
        raise IndexError("cursor is invalid")

    val = lst.cursor.data
    if lst.cursor.next == None:
        lst.cursor = lst.head
    else:
        lst.cursor = lst.cursor.next
    return lst.cursor.data


###########################################################
# LINKED LIST FUNCTIONS
###########################################################

def clear( lst ):
    """
       Make a list empty.
       Parameters:
           lst ( SlList ) - the linked list
       Returns:
           None
    """

    lst.head = None
    lst.size = 0
    lst.cursor = None # invalidate cursor on clear()


def toString(lst):
    """
    Converts our linked list into a string form that is similar to Python's
    printed list.

    Parameters:
        lst (SlList) - The linked list
    Returns:
        A string representation of the list (e.g. '[1,2,3]')
    """

    result = '['
    curr = lst.head
    while not curr == None :
        if curr.next == None :
            result +=  str(curr.data)
        else:
            result += str(curr.data) + ', '
        curr = curr.next
    result += ']'

    return result


def append( lst, value ):
    """
       Add a node containing the value to the end of the list.

       Parameters:
           lst ( SlList ) - The linked list
           value ( any type ) - The data to append to the end of the list
       Returns:
           None
    """

    if lst.head == None :
        lst.head = Node( value,0, None )
        lst.cursor = lst.head
    else:
        curr = lst.head
        while curr.next != None :
            curr = curr.next
        curr.next = Node( value,0, None )
    lst.size += 1

def insertAt( lst, index, value ):
    """
       Insert a new element before the index.

       Parameters:
           lst ( SlList ) - The list to insert value into
           index ( int ) - The 0-based index to insert before
           value ( any type ) - The data to be inserted into the list
       Preconditions:
           0 <= index <= lst.size, raises IndexError exception
       Returns:
           None
    """

    if index < 0 or index > lst.size:
        raise IndexError( str( index ) + ' is out of range.' )

    if index == 0:
        lst.head = Node( value, lst.head )
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        prev.next = Node( value, prev.next )

    lst.size += 1

def get( lst, index ):
    """
       Returns the element that is at index in the list.

       Parameters:
           lst ( SlList ) - The list to insert value into
           index ( int ) - The 0-based index to get
       Preconditions:
           0 <= index < lst.size, raises IndexError exception
       Returns:
           value at the index
    """

    if index < 0 or index >= lst.size:
        raise IndexError( str( index ) + ' is out of range.' )

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    return curr.data

def set( lst, index, value ):
    """
       Sets the element that is at index in the list to the value.

       Parameters:
           lst ( SlList ) - The list to insert value into
           index ( int ) - The 0-based index to set
           value ( any type )
       Preconditions:
           0 <= index < lst.size, raises IndexError exception
       Returns:
           None
    """

    if index < 0 or index >= lst.size:
        raise IndexError( str( index ) + ' is out of range.' )

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    curr.data = value

def pop( lst, index ):
    """
       pop removes and returns the element at index.

       Parameters:
           lst ( SlList ) - The list from which to remove
           index ( int ) - The 0-based index to remove
       Preconditions:
           0 <= index < lst.size, raises IndexError exception
       Returns:
           The value ( any type ) being popped
    """

    if index < 0 or index >= lst.size:
        raise IndexError( str( index ) + ' is out of range.' )

    if index == 0:
        value = lst.head.data
        lst.head = lst.head.next
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        value = prev.next.data
        prev.next = prev.next.next

    lst.size -=1
    lst.cursor = None # invalidate cursor on pop()
    return value

def index( lst, value ):
    """
       Returns the index of the first occurrence of a value in the list

       Parameters:
           lst ( SlList ) - The list to insert value into
           value ( any type ) - The data being searched for
       Preconditions:
           value exists in list, otherwise raises ValueError exception
       Returns:
           The 0-based index of value
    """

    pos = 0
    curr = lst.head
    while not curr == None :
        if curr.data == value:
            return pos

        pos += 1
        curr = curr.next

    raise ValueError( str( value ) + " is not present in the list" )


def createSpin(lst):
    """
    returns random integer on range 1 to two times linked list size
    """
    return randint(1, 2*lst.size)

def getCursor(lst):
    """
    returns data cursor is on
    """
    return lst.cursor.data

def set(lst, value):
    lst.cursor.data = value

