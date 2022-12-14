extern crate reqwest;
extern crate scraper;

use scraper::Selector;
use scraper::Html;

fn main() {
  let url = "https://crypto.com/price";
  let response = reqwest::blocking::get(url).expect("Could not load URL.");
  let raw_html_string = response.text().unwrap();
  
  let html_fragme nt = Html::parse_fragment(&raw_html_string);
  
  let table_selector_string = ".chakra-table css-1qpk7f7";
  
  let table_selector = Selector::parse(table_selector_string).unwrap();
  let head_elements_selector = Selector::parse("thead>tr>th").unwrap(); 
  let row_element s_selector = Selector::parse("tbody>tr").unwrap();
  let row_element_data_selector = Selector::parse("td, th").unwrap();

  let all_tables = html_fragment.select(&table_selector);

  for table in all_tables{
   let head_elements = table.select(&head_elements_selector);
    for head_element in head_elements{
      
    }
    
   let row_elements = table.select(&row_elements_selector);
   for row_element in row_elements{
    for td_element in row_element.select(&row_element_data_selector){
      let prices = html_fragment.select(&).map(|y| y.inner_html());
    }
   }
  }
}
