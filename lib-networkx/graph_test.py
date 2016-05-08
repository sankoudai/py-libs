__author__ = 'quiet road'
import unittest
import networkx as nx

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = nx.Graph()
