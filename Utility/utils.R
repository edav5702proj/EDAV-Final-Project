# Quick render: only work for same-level .rmd file
# fname can be any .Rmd file
quick_build <- function(fname){
  name <- sprintf("%s.Rmd", fname)
  bookdown::render_book(name)
  browseURL(sprintf("docs/%s.html", fname))
}
# Run this to render
quick_build("index")

# Utility function for plotting
# library(reticulate) #nolint
read_all <- function() {
  library(hash)
  filenames <- list.files("Data/data/Magic Kingdom/xysong_python")
  dict <- hash()
  for (csv in filenames){
    dict[[csv]] <- read.csv(sprintf("Data/data/Magic Kingdom/xysong_python/%s", csv)) #nolint
  }
  return(dict)
}

