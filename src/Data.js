

import { sampleProducts } from "./data_clothes";

// List of item categories.
const categories = [
  {
    name: "All categories",
    icon: "list"
  },
  {
    name: "Clothing and Shoes",
    icon: "group"
  },
  {
    name: "Jewelry and Watches",
    icon: "watch"
  },
  {
    name: "Books",
    icon: "menu_book"
  },
  {
    name: "Computers",
    icon: "computer"
  }
];

// Data for rendering menu.
const dataForTheMenu = [
  { name: "Home page", url: "/", icon: "home", id: 0 },
  {
    name: "Product categories",
    id: 1,
    children: categories.map((x, i) => {
      return {
        name: x.name,
        id: i,
        url: "/?category=" + x.name,
        icon: x.icon
      };
    })
  }
];



export { sampleProducts, categories, dataForTheMenu };
