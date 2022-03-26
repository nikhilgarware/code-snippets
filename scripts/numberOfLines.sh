//execute this to check number of lines in directorly only
find  frontend/src/App/Modules/Reports -type f -name '*.jsx' -o -name '*.js' -o -name '*.js' | xargs wc -l | tail -1 