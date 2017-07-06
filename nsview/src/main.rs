#![feature(plugin, custom_derive)]
#![plugin(rocket_codegen)]
extern crate rocket;

use std::fs::File;


#[get("/")]
//fn index() -> content::HTML<String> {
fn index() -> Option<File>{
	File::open("web/index.html").ok()
	
}


fn main() {
	rocket::ignite().mount("/", routes![index]).launch()
}
