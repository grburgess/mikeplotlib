import matplotlib.pyplot as plt


class Plot(object):
    def __init__(self,x='', y=''):
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

        self._ax.set_xlabel(x)
        self._ax.set_ylabel(y)

    @property
    def ax(self):
        return self._ax

    @property
    def fig(self):
        return self._fig
