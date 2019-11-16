import matplotlib.pyplot as plt



class Plot(object):
    def __init__(self):
        """
        Sets up a plot quickly to avoid
        writing:

        fig, ax = plt.subplots()
     
        all the time!

        :returns: 
        :rtype: 

        """

        fig, ax = plt.subplots()

        self._fig = fig
        self._ax = ax

    @property
    def ax(self):
        return self._ax

    @property
    def fig(self):
        return self._fig

