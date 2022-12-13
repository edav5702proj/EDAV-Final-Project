# Quick render: only work for same-level .rmd file
# fname can be any .Rmd file
quick_build <- function(fname) {
  name <- sprintf("%s.Rmd", fname)
  bookdown::render_book(name)
  browseURL(sprintf("docs/%s.html", fname))
}
# Run this to render
quick_build("index")

# Utility function for plotting
# library(reticulate) #nolint
ATTRACTION_NAMES <- c(
  "country bears",
  "7 dwarfs train",
  "pirates of caribbean",
  "astro orbiter",
  "laugh floor",
  "regal carrousel",
  "big thunder mtn",
  "splash mountain",
  "hall of presidents",
  "space mountain",
  "sorcerers of the mk",
  "jungle cruise",
  "mad tea party",
  "princess hall cinderella elena",
  "dumbo",
  "tom land speedway",
  "swiss family tree",
  "magic carpets",
  "tom sawyer island",
  "peoplemover",
  "philharmagic",
  "it s a small world",
  "town sq mickey",
  "carousel of progress",
  "under the sea",
  "barnstormer",
  "winnie the pooh",
  "enchanted tiki rm",
  "princess hall rapunzel tiana",
  "pirate s adventure",
  "liberty sq riverboat",
  "peter pan s flight",
  "haunted mansion",
  "buzz lightyear"
)
process_name <- function(csv){
  return(gsub("  ", "", gsub(".csv", "", gsub("_", " ", csv))))
}

read_all <- function() {
  library(hash)
  filenames <- list.files("Data/data/Magic Kingdom/xysong_python") # nolint
  dict <- hash()
  for (csv in filenames) {
    dict[[process_name(csv)]] <- read.csv(sprintf("Data/data/Magic Kingdom/xysong_python/%s", csv)) # nolint
  }
  return(dict)
}

