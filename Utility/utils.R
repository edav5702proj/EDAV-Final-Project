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
process_name <- function(csv){
  return(gsub("  ", "", gsub(".csv", "", gsub("_", " ", csv))))
}

get_attraction_name <- function(){
  return(lapply(list.files("Data/data/Magic Kingdom/xysong_python"), process_name)) #nolint
}
get_attraction_name()

read_all <- function() {
  library(hash)
  filenames <- list.files("Data/data/Magic Kingdom/xysong_python") # nolint
  dict <- hash()
  for (csv in filenames) {
    dict[[process_name(csv)]] <- read.csv(sprintf("Data/data/Magic Kingdom/xysong_python/%s", csv)) # nolint
  }
  return(dict)
}