// Testacular configuration
// Generated on Sun Mar 10 2013 17:48:19 GMT-0300 (E. South America Standard Time)


// base path, that will be used to resolve files and exclude
basePath = '';


// list of files / patterns to load in the browser
files = [
  JASMINE,
  JASMINE_ADAPTER,
  'sample_data/js/*.js',
  'sample_data/test/*Spec.js'
];


// list of files to exclude
exclude = [
  
];

preprocessors = {
  '**/lib/*.js': 'coverage',
  '../sample_data/js/*.js': 'coverage',
  '../sample_data/test/*Spec.js': 'coverage'
};

// test results reporter to use
// possible values: 'dots', 'progress', 'junit'
reporters = ['coverage'];

coverageReporter = {
  type : 'html',
  dir : '../coverage/',
  file : '../coverage.txt'
}

// web server port
port = 9876;


// cli runner port
runnerPort = 9100;


// enable / disable colors in the output (reporters and logs)
colors = true;


// level of logging
// possible values: LOG_DISABLE || LOG_ERROR || LOG_WARN || LOG_INFO || LOG_DEBUG
logLevel = LOG_INFO;


// enable / disable watching file and executing tests whenever any file changes
autoWatch = false;


// Start these browsers, currently available:
// - Chrome
// - ChromeCanary
// - Firefox
// - Opera
// - Safari (only Mac)
// - PhantomJS
// - IE (only Windows)
browsers = ['PhantomJS'];


// If browser does not capture in given timeout [ms], kill it
captureTimeout = 60000;


// Continuous Integration mode
// if true, it capture browsers, run tests and exit
singleRun = true;
