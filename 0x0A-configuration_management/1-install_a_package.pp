# Downloads the puppet linter version 2.1.1 (using ruby's provider).
package {'puppet-lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
