#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# AyersA, 2022-Dec-12, Added code to the select_cd and add track method 
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODone add code as required
        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID is not an integer')
            print(f'{e.__doc__}')
        for row in table:
            if int(row.cd_id) == int(cd_idx):
                return row
        raise Exception('This CD/Album Index does not exist')


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.
            Exception: Raise when title and length are not a string

        Returns:
            None: DESCRIPTION.

        """
        position = track_info[1]
        title = track_info[2]
        length = track_info[3]
        
        try:
            position = int(position)
        except:
            raise Exception ('Position must be an integer')
        
        try:
            title = str(title)
        except: 
            raise Exception('Title must be a string')
        try:
            length = str(length)
        except:
            raise Exception('Length must be a string')
        
        track_to_add = DC.Track(position, title, length)
        cd.add_track(track_to_add)

