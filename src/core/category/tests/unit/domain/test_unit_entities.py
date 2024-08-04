import unittest
from dataclasses import is_dataclass
from datetime import datetime

from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):
  
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(Category))
  
  def test_constructor(self):  # sourcery skip: extract-duplicate-method
    category = Category(name='Movie')
   
    self.assertEqual(category.name, 'Movie')
    self.assertEqual(category.description, None)
    self.assertEqual(category.is_active, True)
    self.assertIsInstance(category.created_at, datetime)
    
    created_at = datetime.now()
    category = Category(
      name='Movie', 
      description='Some description', 
      is_active= False, 
      created_at=created_at
    )
    
    self.assertEqual(category.name, 'Movie')
    self.assertEqual(category.description, 'Some description')
    self.assertEqual(category.is_active, False)
    self.assertEqual(category.created_at, created_at)
    
  def test_if_created_at_is_generated_in_constructor(self):
    category1 = Category(name='Movie')
    category2 = Category(name='Movie')
    
    self.assertNotEqual(
      category1.created_at.timestamp(),
      category2.created_at.timestamp()
    )